import random
import requests #Please install with PIP: pip install requests

import time

request = None


for count in range(10):
  print('Program Starting...')
  RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=2K1UL7AJ3BY7PQQN&field1='
  RequestToThingspeak +=str((random.randint(1, 100)))
  request = requests.get(RequestToThingspeak)
  print('You got this')
  print(request.text)
  time.sleep(10)