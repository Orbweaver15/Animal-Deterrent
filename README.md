# IoT Mobile Animal Deterrent (Remote Rover)

## 📌 Project Overview
A web-controlled mobile robot designed for remote deterrence and monitoring. The system utilizes a Master-Slave architecture where a Raspberry Pi (Ubuntu Server) hosts a Python Flask control interface, communicating via Serial (UART) to an Arduino microcontroller that drives the hardware.

The robot is accessible from any device on the local network via SSH tunneling or the hosted web dashboard, allowing for low-latency teleoperation.

## 🛠 Tech Stack
* **Software:** Python 3, Flask (Web Framework), HTML/CSS, Arduino C++
* **OS:** Ubuntu Server (running on Raspberry Pi)
* **Hardware:** Raspberry Pi 4, Arduino Uno, 12V DC Motors, MC33886 Dual Motor Driver
* **Communication:** Serial (USB-to-UART), SSH, HTTP

## ⚙️ System Architecture
1.  **Web Interface (Flask):** Users access a local IP address to view controls.
2.  **Server Logic:** Python script captures user inputs (Forward, Back, Stop).
3.  **Serial Communication:** Commands are packetized and sent via USB Serial to the Arduino.
4.  **Actuation:** Arduino parses the string commands and triggers the MC33886 driver to power the motors.

## 🚀 Key Features
* **Local Network Control:** Wireless control via any browser on the same Wi-Fi network.
* **SSH Tunneling:** Remote backend access for diagnostics and server management.
* **High-Torque Drive:** Integrated MC33886 driver for handling high-current 12V motors.
