import random
import requests  #Please install with PIP: pip install requests

import time

request = None


for count in range(3):
  print('Program Starting..')
  RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=2K1UL7AJ3BY7PQQN&field1='
  RequestToThingspeak += str((random.randint(1, 100)))
  RequestToThingspeak += '&field2='
  RequestToThingspeak += str(5);
  RequestToThingspeak += '&field3='
  RequestToThingspeak += str(4);
  RequestToThingspeak += '&field4='
  RequestToThingspeak += str(5);
  request = requests.get(RequestToThingspeak)
  print('You got this')
  print(request.text)
  time.sleep(2)