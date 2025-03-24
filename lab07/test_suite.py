import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# GPIO Setup
GPIO.setmode(GPIO.BOARD)

# PIN Definitions
LED_PIN = 11
LIGHT_SENSOR_CHANNEL = 0
SOUND_SENSOR_CHANNEL = 1

# LED o/p setup
GPIO.setup(LED_PIN, GPIO.OUT)

# HW SPI config
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Thresholds
lux_threshold = 110 # room w/ lights on
sound_threshold = 550 # tapping sound sensor

def blink_led(times, interval):
    for _ in range(times):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(interval)

def read_light_sensor(duration=5, interval=0.1):
    start_time = time.time()
    while time.time() - start_time < duration:
        light_value = mcp.read_adc(LIGHT_SENSOR_CHANNEL)
        if light_value > lux_threshold:
            print(f"{light_value} is BRIGHT")
        else:
            print(f"{light_value} is DARK")
        time.sleep(interval)

def read_sound_sensor(duration=5, interval=0.1):
    start_time = time.time()
    while time.time() - start_time < duration:
        sound_value = mcp.read_adc(SOUND_SENSOR_CHANNEL)
        print(f"Volume: {sound_value}")
        
        if sound_value > sound_threshold:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.1)  # LED on for 100ms
            GPIO.output(LED_PIN, GPIO.LOW)
        
        time.sleep(interval)

try:
    while True:
        print("starting test...\n")

        # Step 1: Blink LED 5 times (500ms on/off)
        blink_led(5, 0.5)

        # Step 2: Read Light Sensor for 5 seconds (100ms interval)
        read_light_sensor()

        # Step 3: Blink LED 4 times (200ms on/off)
        blink_led(4, 0.2)

        # Step 4: Read Sound Sensor for 5 seconds (100ms interval)
        read_sound_sensor()

        print("\nrestarting test...\n")
        time.sleep(2)  # Small delay before restarting loop
finally:
    GPIO.cleanup()  # Clean up GPIO on exit

