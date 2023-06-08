import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

TOY_NAME = "SB-BFEA"

toy = scanner.find_toy(toy_name=TOY_NAME)
with SpheroEduAPI(toy) as sphero:
    sphero.set_main_led(Color(r=0, g=255, b=255))
    sphero.set_speed(speed=60)
    time.sleep(2)
    sphero.set_speed(speed=0)