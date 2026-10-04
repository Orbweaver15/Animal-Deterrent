# IoT Mobile Animal Deterrent (Remote Rover)

## Project Overview

An embedded mobile robotics platform engineered for remote monitoring, surveillance, and deterrence applications. The platform utilizes a hierarchical master-slave architecture: a Raspberry Pi running Ubuntu Server hosts a lightweight Flask web application for telemetry and control, while an Arduino Uno microcontroller executes low-level, real-time motor actuation. Subsystems communicate over a deterministic USB-to-UART serial link, facilitating low-latency teleoperation across local networks or encrypted SSH tunnels.

---

## Technical Specifications

| Domain | Technology / Component | Details |
| :--- | :--- | :--- |
| **Compute (Master)** | Raspberry Pi 4 Model B | Ubuntu Server (ARM64) |
| **Compute (Slave)** | Arduino Uno Rev3 | ATmega328P Microcontroller |
| **Actuation Driver** | MC33886 Dual H-Bridge | Integrated thermal and short-circuit protection |
| **Actuators** | 12V High-Torque Brushed DC Motors | Differential drive configuration |
| **Software Stack** | Python 3, Flask, HTML5, CSS3 | Backend dispatch and control dashboard |
| **Firmware** | Arduino C / C++ (Wiring) | Serial packet parser and PWM state machine |
| **Communication Protocols** | HTTP, SSH Tunneling, UART Serial | Standardized packet exchange at 115200 baud |

---

## System Architecture

```text
[ Client Browser ]
        |
        |  HTTP / Port Forwarding
        v
[ Raspberry Pi 4 (Ubuntu Server) ]
   ├── Flask Application Server
   └── Serial Dispatcher (Python)
        |
        |  UART over USB (/dev/ttyACM0)
        v
[ Arduino Uno Microcontroller ]
   └── Non-blocking Serial Buffer & State Machine
        |
        |  Direction Logic + PWM Signals
        v
[ MC33886 Dual H-Bridge Motor Driver ]
        |
        |  High-Current 12V Delivery
        v
[ 12V DC Actuator Assembly ]
```

### Functional Subsystems

1. **Telemetry & Presentation Layer:** The Flask server serves a responsive dashboard to authorized endpoints on the local subnet or via an authenticated SSH tunnel, exposing discrete directional commands and system telemetry.
2. **Serial Dispatch Pipeline:** The backend processes incoming control requests, validates payloads, and serializes deterministic command packets across the USB-to-UART serial interface.
3. **Firmware & Low-Level Control:** The Arduino firmware implements a non-blocking state machine that monitors the serial buffer, decodes incoming packets, and translates instructions into discrete logic signals and PWM pulses.
4. **Power Regulation & Drive Stage:** The MC33886 dual H-bridge module regulates high-current 12V delivery to the drive motors, incorporating thermal shutdown, under-voltage lockout, and over-current protection for sustained hardware reliability.

---

## Key Capabilities

* **Low-Latency Teleoperation:** Zero-install web dashboard provides immediate vehicle control across local networks.
* **Decoupled Architecture:** Dual-controller design isolates non-deterministic OS network operations from time-critical hardware actuation and fail-safe logic.
* **Secure Remote Administration:** Complete backend access via encrypted SSH tunneling for telemetry logging, system diagnostics, and firmware deployment.
* **Industrial-Grade Motor Protection:** Dual H-bridge architecture provides current protection and thermal management during high-torque operational peaks.
