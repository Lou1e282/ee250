import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(2)
    setText(f"{distance} cm")

    # TODO: read threshold from potentiometer
    threshold = grovepi.analogueRead(0)
    
    # TODO: format LCD text according to threshhold
    space = 13 - len(str(distance))
    if distance < threshold :
      setText(f"{''*space}OBJ PRES")
    else: 
      setText(f"{''*space}{threshold} cm")
  
    
  except IOError:
    print("Error")