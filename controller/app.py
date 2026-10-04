"""Flask web controller for the AnimalDeterrent robot.

Run with:  python app.py
"""

from flask import Flask

import config
from arduino_link import ArduinoLink
from routes import register_routes

app = Flask(__name__)
arduino = ArduinoLink(
    config.ARDUINO_PORT,
    config.BAUD_RATE,
    config.SERIAL_TIMEOUT,
    config.ARDUINO_RESET_DELAY,
)
register_routes(app, arduino)

# Initial connection attempt
arduino.connect()

if __name__ == '__main__':
    try:
        print(f"🚀 Starting Flask server on http://{config.HOST}:{config.PORT}")
        app.run(host=config.HOST, port=config.PORT, debug=False)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    finally:
        arduino.close()
