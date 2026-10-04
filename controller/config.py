"""Settings for the AnimalDeterrent web controller."""

# Arduino serial connection
ARDUINO_PORT = '/dev/arduino_uno'  # Change to your actual port
BAUD_RATE = 9600  # Must match SerialBaudRate in arduino/AnimalDeterrent/robot_config.h
SERIAL_TIMEOUT = 1
ARDUINO_RESET_DELAY = 2  # Seconds to allow for Arduino reset after opening the port

# Web server
HOST = '0.0.0.0'
PORT = 5000

# Commands accepted by the /<key>/<action> endpoint
VALID_KEYS = ('w', 'a', 's', 'd')
VALID_ACTIONS = ('press', 'release')
