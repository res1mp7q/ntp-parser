from bs4 import BeautifulSoup
import requests
import paho.mqtt.client as mqtt

# URL of the NTP score page
url = "https://www.ntppool.org/scores/yourNTPaddress"

# Fetch the HTML content
response = requests.get(url)
html_content = response.text
# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the paragraph containing the score
score_paragraph = soup.find('p', string=lambda text: "Current score:" in (text or ""))

# Define current_score with a default value
current_score = None

# Extract and print the current score
if score_paragraph:
    # Extract the score from the paragraph text
    score_text = score_paragraph.get_text(strip=True)
    current_score_str = score_text.split(":")[-1].split()[0]

    try:
        current_score = float(current_score_str)
        print(f"Current NTP score: {current_score}")
    except ValueError:
        print(f"Error converting '{current_score_str}' to float.")
else:
    print("Score paragraph not found on the page.")

# MQTT configuration
mqtt_broker = "mqtt.excelsior.lan"
mqtt_topic = "ntp/score/state"

# Publish the NTP score to MQTT
client = mqtt.Client()
client.username_pw_set("mqtt-username", "replace_me")
client.connect(mqtt_broker, 1883, 60)

# Always publish the score to MQTT, regardless of its value
client.publish(mqtt_topic, f"{current_score}" if current_score is not None else "Score not available")

client.disconnect()