# Excelsior Wireless Ltd Jimmy Lamont 2023
# A simple NTP Pool dash scraper to publish results to MQTT

from bs4 import BeautifulSoup
import requests
import paho.mqtt.client as mqtt

# URL of the NTP score page
url = "https://www.ntppool.org/scores/yourIPhere"

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
score_line = soup.find(string="Current score:")

# Define current_score with a default value
current_score = None

# Extract and print the current score
if score_line:
    current_score_str = score_line.find_next('span').text.strip()
    try:
        current_score = float(current_score_str)
        print(f"Current NTP score: {current_score}")
    except ValueError:
        print(f"Error converting '{current_score_str}' to float.")
else:
    print("Current score not found on the page.")

# MQTT configuration
mqtt_broker = "mqtt.excelsior.lan"
mqtt_topic = "ntp/score/state"

# Publish the NTP score to MQTT
client = mqtt.Client()
client.username_pw_set("mqtt-username", "replaceme")
client.connect(mqtt_broker, 1883, 60)

# Always publish the score to MQTT, regardless of its value
client.publish(mqtt_topic, f"{current_score}" if current_score is not None else "Score not available")

client.disconnect()