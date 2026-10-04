#ifndef COMMANDS_H
#define COMMANDS_H

#include <Arduino.h>

// Act on one trimmed command line received over serial.
// "w_press", "a_press", "s_press" and "d_press" move the robot;
// any other command (including every "*_release") stops all motors.
void handleCommand(const String &command);

#endif
