import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

TOY_NAME = "BB-EFF7"

toy = scanner.find_toy(toy_name=TOY_NAME)
with SpheroEduAPI(toy) as sphero:
    sphero.set_main_led(Color(r=0, g=255, b=255))
    # Make a square
    # roll at 0 degrees at speed 100 for 1 second
    sphero.roll(0, 255, 1)
    time.sleep(1)
    # roll at 90 degrees at speed 100 for 1 second
    sphero.roll(90, 255, 1)
    time.sleep(1)
    # roll at 180 degrees at speed 100 for 1 second
    sphero.roll(180, 255, 1)
    time.sleep(1)
    # roll at 270 degrees at speed 100 for 1 second
    sphero.roll(270, 255, 1)
    time.sleep(1)

    # we can do better though
    # for loop
    for i in range(4):
        sphero.roll(i * 90, 255, 1)
        time.sleep(1)

    # What if we wanted to roll in any regular polygon?
    # Do some math
    # 360 / num_sides = angle
    # hexagon = 360 / 6 = 60 for example
    num_sides = 6
    angle = 360 / num_sides
    for i in range(num_sides):
        sphero.roll(int(i * angle), 255, 0.7)
        time.sleep(1)

    # let's go back and make a circle
    sphero.set_heading(0)
    for i in range(360):
        sphero.roll(i, 255, 0.02)
        time.sleep(0.02)
