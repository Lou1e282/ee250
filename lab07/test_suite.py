import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPIs
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)
# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#PIN definition
LED_PIN = 11 
LIGHT_SENSOR_CHANNEL = 1   #//// /////////
SOUND_SENSOR_CHANNEL = 2   #///////////  

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_threshold = 0 
sound_threshold = 0 

def blink_led(times, interval):
  for _ in range(times):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(interval)

def read_light_sensor(duration, interval):
  start_time = time.time()
  while time.time() - start_time < duration:
    light_value = mcp.read_adc(LIGHT_SENSOR_CHANNEL) 
    if light_value > lux_threshold:
      print("Bright: %d" %(light_value))
    else:
      print("Dark: %d" %(light_value))
    time.sleep(interval)

def read_sound_sensor(duration, interval):
  start_time = time.time()
  while time.time() - start_time < duration:
    sound_value = mcp.read_adc(SOUND_SENSOR_CHANNEL)
    print("Volume: %d" %(sound_value))
    if sound_value > lux_threshold:
      GPIO.output(LED_PIN, GPIO.HIGH)
      time.sleep(1)
      


while True: 
  time.sleep(0.5) 

  #Following commands control the state of the output

  #GPIO.output(pin, GPIO.HIGH)
  #GPIO.output(pin, GPIO.LOW)

  # get reading from adc 
  # mcp.read_adc(adc_channel)

  #test case
  blink_led(4, 2)
  read_light_sensor()
  read_sound_sensor()
  

  


