/* 
 * This Arduino drives all of the motors on the turing machine using a motor shield.
 */

#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"
#include <Servo.h> 

#define MARKER_SERVO_DOWN       (112)
#define MARKER_SERVO_UP         (90)
#define ERASER_LIFT_SERVO_UP    (255)
#define ERASER_LIFT_SERVO_DOWN  (100)
#define ERASER_SPIN_SERVO_GO    (0)
#define ERASER_SPIN_SERVO_STOP  (255)

int potPin = 2;    // select the input pin for the potentiometer
int ledPin = 13;   // select the pin for the LED
int val = 0;       // variable to store the value coming from the sensor



// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *markerMotor = AFMS.getStepper(200, 2);
Adafruit_StepperMotor *tapeMotor = AFMS.getStepper(200, 1);

// We'll also test out the built in Arduino Servo library
Servo markerServo;
Servo eraserLiftServo;
Servo eraserSpinServo;

void setup() {
  Serial.begin(9600);
  
  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
  // Init our stepper that moves the marker
  markerMotor->setSpeed(1000);  // 10 rpm  
 
  // Init our stepper that feeds the tape 
  tapeMotor->setSpeed(10);
  
  // Attach a servo to pin #10
  markerServo.attach(10);
  eraserLiftServo.attach(9);
  eraserSpinServo.attach(11);
  
  eraserLift();
  eraserStop();
  markerLift();
  //gantryZero();
}



void markerLift() {
  markerServo.write(map(MARKER_SERVO_UP, 0, 255, 0, 180));
}

void markerLower() {
  markerServo.write(map(MARKER_SERVO_DOWN, 0, 255, 0, 180));
}

static uint16_t gantryPosition = 0;

void gantryZero(){
  gantryPosition = 0;
  markerMotor->step(3000, BACKWARD, SINGLE);
  markerMotor->step(1000, FORWARD, DOUBLE);
}

void gantryOut(){
  if(gantryPosition < 1600){
    gantryPosition += 1600;
    markerMotor->step(1600, FORWARD, DOUBLE);
  }
}

void gantryIn(){
  if(gantryPosition >= 1600){
    gantryPosition -= 1600;
    markerMotor->step(1600, BACKWARD, DOUBLE);
  }
}

void eraserLower(){
  eraserLiftServo.write(map(ERASER_LIFT_SERVO_DOWN, 0, 255, 0, 180));
}

void eraserLift(){
  eraserLiftServo.write(map(ERASER_LIFT_SERVO_UP, 0, 255, 0, 180));
}

void eraserSpin(){
  eraserSpinServo.write(map(ERASER_SPIN_SERVO_GO, 0, 255, 0, 180));
}

void eraserStop(){
  eraserSpinServo.write(map(ERASER_SPIN_SERVO_STOP, 0, 255, 0, 180));
}

void tapeMoveLeft() {
  tapeMotor->step(60, BACKWARD, DOUBLE);
}

void tapeMoveRight() {
  tapeMotor->step(60, FORWARD, DOUBLE);
}
void loop() {
  static uint8_t val = 128;
  uint8_t c;
  if(Serial.available()){
    c = Serial.read();
    
    switch(c){
    
      // Eraser functions
      case 'E':
        eraserLift();
        break;
      case 'e':
        eraserLower();
        break;
      case 'S':
        eraserSpin();
        break;
      case 's':
        eraserStop();
        break;
        
      // Marker functions
      case 'M':
        markerLift();
        break;
      case 'm':
        markerLower();
        break;
      case 'G':
        gantryOut();
        break;
      case 'g':
        gantryIn();
        break;
      case 'z':
        gantryZero();
        break;
      
      case '+':
        //markerLift();
        if(val < 252)
          val += 4;
        break;
      case '-':
        //markerLower();
        if(val > 3)
          val -= 4;
        break;
      
      ///
      //  Turing Machine Functions
      ///
       
      // Move tape Left
      case 'l':
        tapeMoveLeft();
        
        Serial.println("done");
        break;
      // Move tape Right
      case 'r':
        tapeMoveRight();
        
        Serial.println("done");
        break;
      
      // Write a 1
      case '1':
        markerLower();
        gantryOut();
        markerLift();
        gantryIn();
        
        Serial.println("done");
        break;
      // Write a 0
      case '0':
        markerLower();
        gantryOut();
        tapeMotor->step(20, FORWARD, DOUBLE);
        gantryIn();
        tapeMotor->step(20, BACKWARD, DOUBLE);
        markerLift();
        
        Serial.println("done");
        break;
        
      // Erase the current tape position
      case 'D':
        tapeMotor->step(125, FORWARD, DOUBLE);
        delay(100);
        eraserLower();
        delay(100);
        eraserSpin();
        delay(100);
        tapeMotor->step(30, BACKWARD, DOUBLE);
        delay(100);
        tapeMotor->step(30, FORWARD, DOUBLE);
        delay(100);
        tapeMotor->step(30, BACKWARD, DOUBLE);
        delay(100);
        tapeMotor->step(30, FORWARD, DOUBLE);
        delay(100);
        eraserStop();
        eraserLift();
        delay(100);
        tapeMotor->step(125, BACKWARD, DOUBLE);
        
        Serial.println("done");
        break;
        
      default:
        Serial.println("unknown");
        break;
    } // End switch
    
    
//    Serial.println(val);
//    eraserSpinServo.write(map(val, 0, 255, 0, 180));
  }
}
