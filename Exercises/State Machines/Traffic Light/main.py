import msvcrt
from time import sleep
from phases import TrafficLightPhase
from traffic_light import TrafficLight

if __name__ == "__main__":
    traffic_light = TrafficLight(
        initial_phase=TrafficLightPhase.GREEN
    )

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().lower()
            if key == b"p":
                traffic_light.request_pedestrian_crossing()

        traffic_light.update()
        traffic_light.render()
        sleep(0.1)
