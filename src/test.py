from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

TOY_NAME = "SB-BFEA"

toy = scanner.find_toy(toy_name=TOY_NAME)
with SpheroEduAPI(toy) as sphero:
    sphero.set_main_led(Color(255,0,0))