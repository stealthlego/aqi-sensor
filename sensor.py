#!/usr/bin/env python3

import requests
import logging
import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt 
import paho.mqtt.publish as publish
import time

logging.basicConfig(level=logging.INFO)

load_dotenv()

api_key = os.getenv('API_KEY')
pw = os.getenv('PASSWORD')

mqttBroker ="192.168.1.199" 
api_string = f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=98103&distance=5&API_KEY=A4578CF7-E787-4494-8C42-6DE04D1B473B'

publish.single('home-assistant/aqi/number', str(0), hostname=mqttBroker)

client = mqtt.Client("ha-client")
client.username_pw_set('home', pw)
client.connect(mqttBroker)
client.loop_start()

while True:
    response = requests.get(url=api_string)
    if response.status_code == 200:
        r = response.json()
        print(r)
        aqi = r[0]['AQI']
        info = client.publish("home-assistant/aqi/number", aqi)
        # logging.info(info.is_published())
        logging.info(f'Just published {aqi} to topic AQI')
        time.sleep(120)
    else:
        logging.warning('Error with API')