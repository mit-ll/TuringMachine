/* Potentiometer 1
 * This is the code for the left potentiometer to maintain tension on the film
 */

#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

int potPin = 2;    // select the input pin for the potentiometer
int val = 0;       // variable to store the value coming from the sensor

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);

void setup() {
  
  // Setup our serial
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  
  AFMS.begin();  // create with the default frequency 1.6KHz
  
  myMotor->setSpeed(100);  // 100 rpm   
}

void loop() {
  
  // Read our potentiometer value
  val = analogRead(potPin);    // read the value from the sensor
  Serial.println(val);
  
  // Based on our thresholds, feed or draw in the film
  if (val > 360) {
    myMotor->step(1, FORWARD, DOUBLE); 
  } else if (val < 350) {
    myMotor->step(1, BACKWARD, DOUBLE); 
  }
}

