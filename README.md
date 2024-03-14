# **OOP Brainstorm for main project for the 4005CMD module (Sahil Ahmed Khan)**

---

See Flowchart for reference: https://lucid.app/lucidchart/ed984ede-dd32-4c56-bbff-c23601887b22/edit?viewport_loc=-26138%2C5625%2C21468%2C9225%2C0_0&invitationId=inv_318f6930-83ee-4ac8-b748-7303208aa1bb

See UML Class Diagram for reference: https://lucid.app/lucidchart/8d9b8317-76aa-49ee-a685-2bf9f0353fcf/edit?viewport_loc=1027%2C663%2C658%2C283%2CHWEp-vi-RSFO&invitationId=inv_7421f249-8ca8-4e6a-ae5e-593140d27fc8 

# **Classes**

## **1. Configuration (Optional)**

**Description:** Stores configuration parameters for a client (sampling rate, MQTT details).

**Attributes:**

- mqttBrokerAddress: string
- mqttClientId: string
- mqttTopic: string
- samplingRate: int

**Methods:** N/A → (Class is used to store data)

## **2. WaveTrackerSensor**

**Description:** Gathers information about the wave that's been found (how tall it is, how long it lasts, which way it's going, measurements, etc…)

**Attributes:**

- serialNumber: string
- location: string
- samplingRate: int
- /WAVES
    - timestamp: datetime
    - amplitude: float
    - period: float
    - waveDirection: float
    - frequency: float
    - fuel: float
- /WIND
    - windSpeed: float
    - windDirection: float
- /WATER
    - waterTemperature: float
    - waterSalinity: float

**Methods:**

- getData()
    - Returns all data about a wave
- getWaveData()
    - Returns Data about /WAVES topic
- getWindData()
    - Returns Data about /WIND topic
- getWaterData()
    - Returns Data about /WATER topic

## **3. MQTTClient**

**Description:** Handles communication with the MQTT broker using the MQTT protocol.

**Attributes:**

- brokerAddress: string
- clientId: string
- topic: string

**Methods:**

- on_connect(client, userdata, flags, rc)
    - Establishes connection to broker
- on_publish(client, userdata, mid )
    - Publishes message to a topic to broker
- on_disconnect(client, userdata, rc)
    - Closes connection to the broker
- on_message(client, userdata, msg)
    - To receive messages from broker

# **Important Notes**

- Each Boat (e.g., Boat1, Boat2) should be its own unique file to test different boats.
- Each Laptop is an object for the MQTTClient class.
- So, Team 1 and Team 2 are created by making Laptop Objects in each Boat File (Boat1, Boat2, etc…)
