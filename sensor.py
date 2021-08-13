import requests
import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt 
import paho.mqtt.publish as publish
import time

load_dotenv()

api_key = os.getenv('API_KEY')
pw = os.getenv('PASSWORD')

mqttBroker ="192.168.1.199" 
api_string = f'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=98103&date=2021-08-01&distance=2&API_KEY={api_key}'

publish.single('home-assistant/aqi/number', str(0), hostname=mqttBroker)

client = mqtt.Client("ha-client")
client.username_pw_set('home', pw)
client.connect(mqttBroker)
client.loop_start()

while True:
    response = requests.get(url=api_string)
    aqi = response.json()[0]['AQI']
    info = client.publish("home-assistant/aqi/number", aqi)
    print(info.is_published())
    print(f'Just published {aqi} to topic AQI')
    time.sleep(10)