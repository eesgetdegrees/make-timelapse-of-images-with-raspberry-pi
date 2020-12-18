from time import sleep
from picamera import PiCamera
from sense_hat import SenseHat

# Set up camera
cam = PiCamera()
cam.resolution = (1920, 1080)

# Turn green pixel on to indicate script is running
s = SenseHat()
s.clear()
s.set_pixel(0, 0, (0, 255, 0))

# Capture initial image
cam.capture('/home/pi/garbage.jpg')
sleep(1)

# Define some things
h = 6 # Hours to run for
t = 5 # Minutes between pictures

# Take a picture once every five minutes
for i in range((60/t)*h):
    cam.capture('/home/pi/image_%d.jpg'%i)
    sleep(60*t)

# Turn off LED to indicate script is finished
s.clear()
