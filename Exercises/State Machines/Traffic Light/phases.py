from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class _TrafficLightPhase:
    red: bool
    amber: bool
    green: bool
    duration_s: int


class TrafficLightPhase(Enum):
    GREEN = _TrafficLightPhase(False, False, True, 5)
    AMBER = _TrafficLightPhase(False, True, False, 2)
    RED = _TrafficLightPhase(True, False, False, 5)
    RED_AMBER = _TrafficLightPhase(True, True, False, 2)

    def next_phase(
        self
    ) -> TrafficLightPhase:
        return PHASE_TRANSITIONS[self]

PHASE_TRANSITIONS = {
    TrafficLightPhase.GREEN: TrafficLightPhase.AMBER,
    TrafficLightPhase.AMBER: TrafficLightPhase.RED,
    TrafficLightPhase.RED: TrafficLightPhase.RED_AMBER,
    TrafficLightPhase.RED_AMBER: TrafficLightPhase.GREEN
}
