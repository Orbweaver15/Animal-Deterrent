#define FrontMotorIn1 8 
#define FrontMotorIn2 9 //PWM pin
#define FrontMotorIn3 10 //PWM Pin
#define FrontMotorIn4 11 //PWM Pin
#define BackMotorIn1 3 //PWM Pin
#define BackMotorIn2 2 
#define BackMotorIn3 4 
#define BackMotorIn4 5 //PWM Pin

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH); //
  
  // Initialize motor pins
  pinMode(FrontMotorIn1, OUTPUT);
  pinMode(FrontMotorIn2, OUTPUT);
  pinMode(FrontMotorIn3, OUTPUT);
  pinMode(FrontMotorIn4, OUTPUT);
  pinMode(BackMotorIn1, OUTPUT);
  pinMode(BackMotorIn2, OUTPUT);
  pinMode(BackMotorIn3, OUTPUT);
  pinMode(BackMotorIn4, OUTPUT);
  
  Serial.println("Use WASD to navigate the robot");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "w_press") 
    {
      Serial.println("Moving forward");
      digitalWrite(FrontMotorIn1, HIGH);
      digitalWrite(FrontMotorIn4, HIGH);
      analogWrite(BackMotorIn1, 180);
      analogWrite(BackMotorIn4, 180);
    }
    else if (command == "a_press") 
    {
      Serial.println("Moving left");
      digitalWrite(FrontMotorIn1, HIGH);
      analogWrite(FrontMotorIn3, 180);
      analogWrite(BackMotorIn1, 180);
      digitalWrite(BackMotorIn3, HIGH);
    }
    else if (command == "s_press") {
      Serial.println("Moving backward");
      analogWrite(FrontMotorIn2, 180);
      analogWrite(FrontMotorIn3, 180);
      digitalWrite(BackMotorIn2, HIGH);
      digitalWrite(BackMotorIn3, HIGH);
    }
    else if (command == "d_press") {
      Serial.println("Moving right");
      analogWrite(FrontMotorIn2, 180);
      digitalWrite(FrontMotorIn4, HIGH);
      digitalWrite(BackMotorIn2, HIGH);
      analogWrite(BackMotorIn4, 180);
    }
    else
    {
      digitalWrite(FrontMotorIn1, LOW);
      digitalWrite(FrontMotorIn2, LOW);
      digitalWrite(FrontMotorIn3, LOW);
      digitalWrite(FrontMotorIn4, LOW);
      digitalWrite(BackMotorIn1, LOW);
      digitalWrite(BackMotorIn2, LOW);
      digitalWrite(BackMotorIn3, LOW);
      digitalWrite(BackMotorIn4, LOW);
    }
  }
}
