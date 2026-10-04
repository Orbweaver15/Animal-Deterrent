#include <Arduino.h>

#include "commands.h"
#include "motors.h"

void handleCommand(const String &command) {
  if (command == "w_press")
  {
    Serial.println("Moving forward");
    moveForward();
  }
  else if (command == "a_press")
  {
    Serial.println("Moving left");
    moveLeft();
  }
  else if (command == "s_press")
  {
    Serial.println("Moving backward");
    moveBackward();
  }
  else if (command == "d_press")
  {
    Serial.println("Moving right");
    moveRight();
  }
  else
  {
    stopMotors();
  }
}
