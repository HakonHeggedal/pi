from blinkt import set_pixel, set_brightness, show, clear
import time

clear()
set_brightness(0.1)
set_pixel(0, 255, 255, 255)
show()

print(123)
time.sleep(20)
print(12345678)
