#include <Arduino.h>

#include "motors.h"
#include "pins.h"
#include "robot_config.h"

void motorsInit() {
  pinMode(FrontMotorIn1, OUTPUT);
  pinMode(FrontMotorIn2, OUTPUT);
  pinMode(FrontMotorIn3, OUTPUT);
  pinMode(FrontMotorIn4, OUTPUT);
  pinMode(BackMotorIn1, OUTPUT);
  pinMode(BackMotorIn2, OUTPUT);
  pinMode(BackMotorIn3, OUTPUT);
  pinMode(BackMotorIn4, OUTPUT);
}

void moveForward() {
  digitalWrite(FrontMotorIn1, HIGH);
  digitalWrite(FrontMotorIn4, HIGH);
  analogWrite(BackMotorIn1, MotorSpeed);
  analogWrite(BackMotorIn4, MotorSpeed);
}

void moveLeft() {
  digitalWrite(FrontMotorIn1, HIGH);
  analogWrite(FrontMotorIn3, MotorSpeed);
  analogWrite(BackMotorIn1, MotorSpeed);
  digitalWrite(BackMotorIn3, HIGH);
}

void moveBackward() {
  analogWrite(FrontMotorIn2, MotorSpeed);
  analogWrite(FrontMotorIn3, MotorSpeed);
  digitalWrite(BackMotorIn2, HIGH);
  digitalWrite(BackMotorIn3, HIGH);
}

void moveRight() {
  analogWrite(FrontMotorIn2, MotorSpeed);
  digitalWrite(FrontMotorIn4, HIGH);
  digitalWrite(BackMotorIn2, HIGH);
  analogWrite(BackMotorIn4, MotorSpeed);
}

void stopMotors() {
  digitalWrite(FrontMotorIn1, LOW);
  digitalWrite(FrontMotorIn2, LOW);
  digitalWrite(FrontMotorIn3, LOW);
  digitalWrite(FrontMotorIn4, LOW);
  digitalWrite(BackMotorIn1, LOW);
  digitalWrite(BackMotorIn2, LOW);
  digitalWrite(BackMotorIn3, LOW);
  digitalWrite(BackMotorIn4, LOW);
}
