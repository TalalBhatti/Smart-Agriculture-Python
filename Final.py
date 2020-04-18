import random
import requests #Please install with PIP: pip install requests
import time
import RPi.GPIO as GPIO
import dht11
import random
import requests  #Please install with PIP: pip install requests
import time
import board
import busio

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
p = GPIO.PWM(12, 50)
p.start(7.5)
#GPIO.cleanup()

# read data using Pin GPIO21
instance = dht11.DHT11(pin=21)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
channel = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
rain = GPIO.input(channel)
chan = AnalogIn(ads, ADS.P0)
chan2 = AnalogIn(ads, ADS.P1)
chan3 = AnalogIn(ads, ADS.P2)


def callback(channel):
        if rain == True:
               print (rain)
        elif rain == False:
                print ("No Rain Detected!")
             
                
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

while True:
    
    soil=(((chan.voltage + chan2.voltage + chan3.voltage)/3)*24.4140)
    result = instance.read()
    time.sleep(2)
    print(soil)
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        request = None
        
    #for count in range(2):
        if rain == True:
            RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=VZAUW5W4CYP560U9&field1='+str(result.temperature) +'&field2='+str(result.humidity) +'&field3=' +str(soil) +'&field4=' +str(1)
            request = requests.get(RequestToThingspeak)
            print('not Raining')
                #time.sleep(2)
        if rain == False:
            RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=VZAUW5W4CYP560U9&field1='+str(result.temperature) +'&field2='+str(result.humidity) +'&field3=' +str(soil) +'&field4=' +str(0)
            request = requests.get(RequestToThingspeak)
            print('Raining')
               # time.sleep(2)

       # Algo
        if rain==True and soil<50:
           GPIO.setmode(GPIO.BOARD)
           GPIO.setup(12, GPIO.OUT)
           p = GPIO.PWM(12, 50)
           p.start(7.5)
           try:
               while True:
                   p.ChangeDutyCycle(7.5)  # turn towards 90 degree
                   time.sleep(15000) # sleep 1 second
                   p.ChangeDutyCycle(2.5)
                   time.sleep(1)
           except:
               break
        

            
        if rain==False and soil<50:
            while(soil<50):
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)         
                GPIO.setup(18,GPIO.OUT)
                     
                GPIO.output(18,GPIO.HIGH)
                     
                time.sleep(3)

#request = None



#for count in range(10):
 # print('Program Starting...')
  #RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=2K1UL7AJ3BY7PQQN&field1='+str(result.temperature)
  #RequestToThingspeak +=str(result.humidity)
  #request = requests.get(RequestToThingspeak)
  #print('You got this')
  #print(request.text)
  #time.sleep(10)
