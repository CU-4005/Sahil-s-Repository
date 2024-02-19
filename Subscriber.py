import paho.mqtt.client as mqtt
import random
import mqtt1 as mqtt1
import time

# MQTT Broker
broker_address = "broker.hivemq.com"
broker_port = 1883

# Gathering topics
Topic_list = mqtt1.boat1_topics

# Function to see messages in topic
def on_message(client, userdata, message):
    print(f"Received message: { str( message.payload.decode("utf-8") )} on topic {message.topic}") #Contents first then Topic

# Setting the callback function for receiving messages
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([(Topic_list[0], 0), (Topic_list[1], 0), (Topic_list[2], 0),
                      (Topic_list[3], 0), (Topic_list[4], 0)])

# Starting and Stopping Loop of receiving messages
ClientA = mqtt.Client("ClientA")
ClientA.on_message = on_message
ClientA.on_connect = on_connect
ClientA.connect(broker_address, broker_port)

ClientA.loop_start()


time.sleep(random.randint(60,120))
ClientA.loop_stop()