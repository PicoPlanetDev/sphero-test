import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

toy = scanner.find_toy()
with SpheroEduAPI(toy) as sphero:
    num_tosses = 0

    def on_freefall(sphero):
        sphero.set_main_led_color(Color(r=255, g=0, b=0))

    def on_landing(sphero):
        sphero.set_main_led_color(Color(r=0, g=255, b=0))
        num_tosses += 1
        sphero.set_matrix_character(str(num_tosses), Color(r=0, g=0, b=255))
        if num_tosses == 10:
            sphero.scroll_matrix_text('You win!', Color(r=0, g=0, b=255), 10, wait=True)