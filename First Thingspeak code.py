import random
import threading
import urllib.request
import requests

# Define a function that will post on server every 15 Seconds

def thingspeak_post():
    threading.Timer(15, thingspeak_post).start()
    val = random.randint(1, 30)
    URl = 'https://api.thingspeak.com/update?api_key='
    KEY = '2K1UL7AJ3BY7PQQN'
    HEADER = '&field1={}&field2={}'.format(val, val)
    NEW_URL = URl + KEY + HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)
    if __name__ == '__main__':
        thingspeak_post()
