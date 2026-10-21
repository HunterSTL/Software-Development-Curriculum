from time import monotonic
from phases import TrafficLightPhase

BG_RED     = '\033[41m'
BG_YELLOW  = '\033[43m'
BG_GREEN   = '\033[42m'
BG_RESET   = '\033[49m'


class TrafficLight:
    def __init__(
        self,
        initial_phase: TrafficLightPhase
    ) -> None:
        self._current_phase: TrafficLightPhase = initial_phase
        self._phase_start_time: float = monotonic()
        self._pedestrian_crossing_requested: bool = False
        self._render_required: bool = True

    def update(
        self
    ) -> None:
        elapsed_time_s = monotonic() - self._phase_start_time

        if elapsed_time_s > self._current_phase_duration():
            self._advance_phase()

    def render(
        self
    ) -> None:
        if not self._render_required:
            return

        red_light = BG_RED + "   " + BG_RESET if self._current_phase.value.red else "   "
        amber_light = BG_YELLOW + "   " + BG_RESET if self._current_phase.value.amber else "   "
        green_light = BG_GREEN + "   " + BG_RESET if self._current_phase.value.green else "   "

        representation = [
            "╔═══╗",
            "║" + red_light + "║",
            "╠═══╣",
            "║" + amber_light + "║",
            "╠═══╣",
            "║" + green_light + "║",
            "╚═══╝"
        ]

        if self._pedestrian_crossing_requested:
            representation.append("Pedestrian crossing requested")

        print("\n".join(representation))
        self._render_required = False

    def request_pedestrian_crossing(
        self
    ) -> None:
        self._render_required = True
        self._pedestrian_crossing_requested = True

    def _advance_phase(
        self
    ) -> None:
        self._render_required = True
        self._current_phase = self._current_phase.next_phase()

        if self._current_phase == TrafficLightPhase.RED:
            self._pedestrian_crossing_requested = False #red phase consumes the request

        self._phase_start_time = monotonic()

    def _current_phase_duration(
        self
    ) -> int:
        if self._current_phase == TrafficLightPhase.RED and self._pedestrian_crossing_requested:
            return 10   #pedestrian crossing request increases the duration of the RED phase to 10s
        return self._current_phase.value.duration_s
