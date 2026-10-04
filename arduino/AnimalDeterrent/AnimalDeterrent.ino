#include "commands.h"
#include "motors.h"
#include "pins.h"
#include "robot_config.h"

void setup() {
  Serial.begin(SerialBaudRate);
  pinMode(StatusLedPin, OUTPUT);
  digitalWrite(StatusLedPin, HIGH);

  // Initialize motor pins
  motorsInit();

  Serial.println("Use WASD to navigate the robot");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    handleCommand(command);
  }
}
