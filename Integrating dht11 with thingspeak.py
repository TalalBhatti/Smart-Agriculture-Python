import random
import requests #Please install with PIP: pip install requests
import time
import RPi.GPIO as GPIO
import dht11


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21
instance = dht11.DHT11(pin=21)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

    time.sleep(1)

request = None



for count in range(10):
  print('Program Starting...')
  RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=2K1UL7AJ3BY7PQQN&field1='
  RequestToThingspeak +=str((random.randint(1, 100)))
  request = requests.get(RequestToThingspeak)
  print('You got this')
  print(request.text)
  time.sleep(10)
