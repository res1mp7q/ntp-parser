# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import paho.mqtt.client as mqtt
from bs4 import BeautifulSoup
url = "https://www.ntppool.org/scores/50.208.57.188"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
score_line = soup.find(string="Current score:")

# Define current_score with a default value
current_score = None

if score_line:
    current_score_str = score_line.find_next('span').text.strip()
    try:
        current_score = float(current_score_str)
        print(f"Current NTP score: {current_score}")
    except ValueError:
        print(f"Error converting '{current_score_str}' to float.")

# Now you can proceed to the MQTT publishing part if needed.
if current_score is not None and current_score > 10.0:
    mqtt_broker = "your_mqtt_broker_address"
    mqtt_topic = "your_mqtt_topic"

    client = mqtt.Client()
    client.connect(mqtt_broker, 1883, 60)
    client.publish(mqtt_topic, f"Current NTP score: {current_score}")
    client.disconnect()
elif current_score is None:
    print("Current score not found on the page.")
else:
    print("Current score is not greater than 10.0.")


if current_score > 10.0:
    mqtt_broker = "mqtt.excelsior.lan"
    mqtt_topic = "ntp/score/state"
    client.username_pw_set("mqtt1", "replaceme")
    client = mqtt.Client()
    client.connect(mqtt_broker, 1883, 60)
    client.publish(mqtt_topic, f"{current_score}")
    client.disconnect ()