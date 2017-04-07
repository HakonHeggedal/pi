#!/usr/bin/python

import time
import requests
import blinkt
import sys


RED =  (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
PURPLE = (128,0,128)

brightness = float(sys.argv[1]) if len(sys.argv) >= 2 else 0.1
wait = float(sys.argv[2]) if len(sys.argv) >= 3 else 1


blinkt.clear()

blinkt.set_all( *(PURPLE+(brightness,)) )

for pos in range(blinkt.NUM_PIXELS):
    r = requests.get("https://www.google.com")
    
    status_color = GREEN if r.status_code is 200 else RED if r.status_code is 404 else BLUE
    blinkt.set_pixel(*((pos,)+status_color+(brightness,)))
    blinkt.show()
    time.sleep(wait)


#blinkt.set_clear_on_exit(False)

