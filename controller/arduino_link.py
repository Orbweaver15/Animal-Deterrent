"""Serial link to the Arduino that drives the robot's motors."""

import time
from threading import Lock

import serial


class ArduinoLink:
    """Owns the serial connection: connecting, auto-reconnecting and sending."""

    def __init__(self, port, baud_rate, timeout, reset_delay):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.reset_delay = reset_delay
        self._serial = None
        self._lock = Lock()

    @property
    def is_open(self):
        return self._serial is not None and self._serial.is_open

    def connect(self):
        """Initialize or reconnect to Arduino"""
        try:
            with self._lock:
                if self._serial:
                    self._serial.close()
                self._serial = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
                time.sleep(self.reset_delay)  # Allow for Arduino reset
                print("✅ Arduino connected!")
                return True
        except serial.SerialException as e:
            print(f"❌ Arduino connection failed: {str(e)}")
            self._serial = None
            return False

    def ensure_connected(self):
        """Auto-reconnect mechanism"""
        if not self.is_open:
            print("⚠ Attempting Arduino reconnection...")
            return self.connect()
        return True

    def send(self, command):
        """Write a command string to the Arduino."""
        with self._lock:
            self._serial.write(command.encode())

    def close(self):
        if self.is_open:
            self._serial.close()
            print("🔌 Arduino connection closed")
