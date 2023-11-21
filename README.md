NTP Score Parser
Overview

This Python script fetches the NTP (Network Time Protocol) score from a specified URL, parses the HTML content, and publishes the result to a private MQTT server.
Requirements

    Python 3
    requests library
    beautifulsoup4 library
    paho-mqtt library

You can install the required libraries using the following command:

bash

pip install requests beautifulsoup4 paho-mqtt

Usage

    Clone the repository:

    bash

git clone https://github.com/yourusername/ntp-parser.git
cd ntp-parser

Open the main.py file and update the following variables:

    url: The URL of the NTP score page.
    mqtt_broker: The address of your MQTT broker.
    mqtt_topic: The MQTT topic to which the script will publish the NTP score.

Run the script:

bash

    python parser.py

The script will fetch the NTP score, print it to the console, and publish it to the specified MQTT topic if it's higher than the threshold (10.0).
Notes

    Ensure that your MQTT broker is running and accessible.
    Adjust the code as needed based on the HTML structure of the NTP score page.

Automate parser to run every 60 minutes and post results

    $ crontab -e

At the bottom of your crontab:

    * */1 * * * python3 /home/user/ntp-parser/parser.py > /dev/null 2>&1

