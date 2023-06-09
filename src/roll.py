import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

TOY_NAME = "SB-BFEA"

toy = scanner.find_toy(toy_name=TOY_NAME)
with SpheroEduAPI(toy) as sphero:
    sphero.set_main_led(Color(r=0, g=255, b=255))
    # Make a square
    # roll at 0 degrees at speed 100 for 1 second
    sphero.roll(0, 100, 1)
    # roll at 90 degrees at speed 100 for 1 second
    sphero.roll(90, 100, 1)
    # roll at 180 degrees at speed 100 for 1 second
    sphero.roll(180, 100, 1)
    # roll at 270 degrees at speed 100 for 1 second
    sphero.roll(270, 100, 1)

    # we can do better though
    # for loop
    for i in range(4):
        sphero.roll(i * 90, 100, 1)
        time.sleep(1)

    # What if we wanted to roll in any regular polygon?
    # Do some math
    # 360 / num_sides = angle
    # hexagon = 360 / 6 = 60 for example
    num_sides = 6
    angle = 360 / num_sides
    for i in range(num_sides):
        sphero.roll(int(i * angle), 100, 0.5)
        time.sleep(1)

    # let's go back and make a circle
    sphero.set_heading(0)
    sphero.set_speed(100)
    sphero.spin(360,2)
    sphero.set_speed(0)    
