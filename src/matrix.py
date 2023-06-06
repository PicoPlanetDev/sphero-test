import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

toy = scanner.find_toy()
with SpheroEduAPI(toy) as sphero:
    # Make the matrix show Hello World
    text_color = Color(r=255, g=0, b=0)
    sphero.set_matrix_character('H', text_color)
    time.sleep(0.5)
    sphero.set_matrix_character('e', text_color)
    time.sleep(0.5)
    sphero.set_matrix_character('l', text_color)
    time.sleep(0.5)
    sphero.set_matrix_character('l', text_color)
    time.sleep(0.5)
    sphero.set_matrix_character('o', text_color)
    time.sleep(0.5)

    # This is very time consuming to write
    letters = ['H', 'e', 'l', 'l', 'o']
    text_color = Color(r=0, g=255, b=0)
    for letter in letters:
        sphero.set_matrix_character(letter, text_color)
        time.sleep(0.5)

    # What about more text?
    text = 'Hello World'
    text_color = Color(r=0, g=0, b=255)
    sphero.scroll_matrix_text(text, text_color, 10, wait=True)

    # Or an animation?