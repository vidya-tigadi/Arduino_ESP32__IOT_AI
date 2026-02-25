🌡 IoT Temperature & Humidity Monitoring System with Cloud Dashboard

An end-to-end IoT system using ESP32 + DHT11 integrated with Arduino IoT Cloud to monitor real-time temperature and humidity, and remotely control an LED from a cloud dashboard.

🚀 Project Overview

This project demonstrates:

Real-time environmental sensing using DHT11

ESP32 WiFi connectivity

Cloud variable synchronization

Remote LED control via dashboard

Live IoT visualization

        +------------------+
        |   DHT11 Sensor   |
        | (Temp & Humidity)|
        +--------+---------+
                 |
                 v
        +------------------+
        |      ESP32       |
        |  - WiFi Enabled  |
        |  - Reads Sensor  |
        |  - Controls LED  |
        +--------+---------+
                 |
                 | WiFi
                 v
        +----------------------+
        |   Arduino IoT Cloud  |
        |  Dashboard           |
        |  - Temp Gauge        |
        |  - Humidity Gauge    |
        |  - LED Switch        |
        +----------------------+

🔌 Hardware Components

ESP32 Dev Module

DHT11 Temperature & Humidity Sensor

LED

220Ω Resistor

Jumper wires

Breadboard


☁️ Cloud Variables

Configured inside Arduino IoT Cloud:

Variable Name	Type	Permission
temperature	float	Read Only
humidity	float	Read Only
ledStatus	bool	Read & Write

🧠 System Algorithm
Device Side

Connect ESP32 to WiFi.

Connect to Arduino IoT Cloud.

Read temperature & humidity every 2 seconds.

Update cloud variables.

Check LED status variable.

Turn LED ON/OFF accordingly.

Repeat.



📊 Dashboard Features

🌡 Real-time Temperature Gauge

💧 Real-time Humidity Gauge

💡 LED Toggle Switch

Remote LED control works instantly via cloud sync.


📈 Sample Output
Temperature (°C)	Humidity (%)	LED Status
25.4	60	ON
25.6	59	OFF


🛠 Tech Stack

ESP32

Arduino IDE

DHT Sensor Library

WiFi

Cloud IoT Integration

Embedded C++


🔮 Future Enhancements

Historical Data Logging

Email Alerts on Threshold

MQTT Broker Integration

Edge AI for Anomaly Detection

Docker-based Backend Logger
