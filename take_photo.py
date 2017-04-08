import picamera
import sys

filename = str(sys.argv[1])

camera = picamera.PiCamera()
camera.capture(filename)
