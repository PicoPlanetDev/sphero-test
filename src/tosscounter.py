from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import time

TOY_NAME = "SB-BFEA"

toy = scanner.find_toy(toy_name=TOY_NAME)
with SpheroEduAPI(toy) as sphero:
    # initialize the sphero communication by setting its color
    sphero.set_main_led(Color(255,0,0))

    # int for number of tosses
    num_tosses = 0
    # two bools for state machine
    falling = False
    lastFalling = False

    # while loop (I used gas in a car example you can drive while the gas > 0)
    while True:
        # conditional to update current falling status
        if sphero.get_acceleration()['z'] < 0.1:
            falling = True
        else:
            falling = False
        
        # determine whether to trigger increase
        if (falling == True and lastFalling == False):
            # increment
            num_tosses = num_tosses + 1

            # show the number of tosses
            sphero.scroll_matrix_text(str(num_tosses), Color(0,0,255), 30, False)

            # check if win condition
            if num_tosses >= 10:
                sphero.scroll_matrix_text(str("You win!"), Color(0,255,0), 30, False)
                time.sleep(2)
                break # exit the loop

        # make the lastFalling variable equal to the current, because current
        # will then be updated next loop through
        lastFalling = falling
