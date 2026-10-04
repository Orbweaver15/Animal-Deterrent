#ifndef MOTORS_H
#define MOTORS_H

// Set all motor driver pins to OUTPUT
void motorsInit();

void moveForward();
void moveLeft();
void moveBackward();
void moveRight();

// Drive every motor pin LOW
void stopMotors();

#endif
