import paho.mqtt.client as mqtt
import random
import time

# MQTT Broker
broker_address = "broker.hivemq.com"
broker_port = 1883

# Topics
ocean_wave_topic = "ocean/wave"
ocean_temperature_topic = "ocean/temperature"
ship_fuel_topic = "ship/fuel"
ship_acceleration_topic = "ship/acceleration"
ship_location_topic = "ship/location"

# Boat 1 publisher
boat1_topics = [ocean_wave_topic, ocean_temperature_topic, ship_fuel_topic,
                ship_acceleration_topic, ship_location_topic]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([(ocean_wave_topic, 0), (ocean_temperature_topic, 0), (ship_fuel_topic, 0),
                      (ship_acceleration_topic, 0), (ship_location_topic, 0)])


def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    
    if msg.topic == ocean_wave_topic:
        # Handle ocean wave data
        pass
    elif msg.topic == ocean_temperature_topic:
        # Handle ocean temperature data
        pass
    elif msg.topic == ship_fuel_topic:
        # Handle ship fuel data
        pass
    elif msg.topic == ship_acceleration_topic:
        # Handle ship acceleration data
        pass
    elif msg.topic == ship_location_topic:
        # Handle ship location data
        pass

def boat1_publisher():
    client = mqtt.Client("Boat1_Publisher")
    client.connect(broker_address, broker_port)

    while True:
        # Generate random data for boat 1
        ocean_wave_frequency = random.uniform(0, 10)
        ocean_wave_amplitude = random.uniform(0, 5)
        ocean_temperature = random.uniform(0, 30)
        ship_fuel_used = random.uniform(0, 100)
        ship_acceleration = random.uniform(0, 10)
        ship_location = (random.uniform(-90, 90), random.uniform(-180, 180))

        # Publish data to broker
        client.publish(ocean_wave_topic, str(ocean_wave_frequency))
        client.publish(ocean_wave_topic, str(ocean_wave_amplitude))
        client.publish(ocean_temperature_topic, str(ocean_temperature))
        client.publish(ship_fuel_topic, str(ship_fuel_used))
        client.publish(ship_acceleration_topic, str(ship_acceleration))
        client.publish(ship_location_topic, str(ship_location))

        time.sleep(1)  # Publish every second

if __name__ == "__main__":
    
    # client_subscriber = mqtt.Client("Subscriber")
    # client_subscriber.on_connect = on_connect
    # client_subscriber.on_message = on_message

    # client_subscriber.connect(broker_address, broker_port, 60)

    # # Start the subscriber client loop in a separate thread
    # client_subscriber.loop_start()

    # Start publishers for Boat 1
    boat1_publisher()