import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

TOY_NAME = "BB-EFF7"

toy = scanner.find_toy(toy_name=TOY_NAME)
with SpheroEduAPI(toy) as sphero:
    # Set the color to red
    sphero.set_main_led(Color(r=255, g=0, b=0))
    time.sleep(1)

    # Set the color to white
    sphero.set_main_led(Color(r=255, g=255, b=255))
    time.sleep(1)

    # Set the color to cyan
    sphero.set_main_led(Color(r=0, g=255, b=255))

    # Set the color to a custom color
    # 4da0f4 is a nice blue, but you can use any hex color
    # 4d is the red component, a0 is the green component, f4 is the blue component
    # 4d is 77 in decimal, a0 is 160 in decimal, f4 is 244 in decimal
    sphero.set_main_led(Color(r=77, g=160, b=244))

    # Cycle through the rainbow
    red = 255
    green = 0
    blue = 0
    delay = 0.001 # 5 milliseconds
    for i in range(255):
        sphero.set_main_led(Color(r=red, g=green, b=blue))
        green += 1
        time.sleep(delay)

    for i in range(255):
        sphero.set_main_led(Color(r=red, g=green, b=blue))
        red -= 1
        time.sleep(delay)

    for i in range(255):
        sphero.set_main_led(Color(r=red, g=green, b=blue))
        blue += 1
        time.sleep(delay)

    for i in range(255):
        sphero.set_main_led(Color(r=red, g=green, b=blue))
        green -= 1
        time.sleep(delay)

    for i in range(255):
        sphero.set_main_led(Color(r=red, g=green, b=blue))
        red += 1
        time.sleep(delay)

    for i in range(255):
        sphero.set_main_led(Color(r=red, g=green, b=blue))
        blue -= 1
        time.sleep(delay)
        