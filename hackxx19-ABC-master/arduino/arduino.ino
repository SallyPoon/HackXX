//This demo is used for testing the Motor module.
#include "UCMotor.h"
#include <Servo.h>

#define SERVO_PIN 10

UC_DCMotor leftMotor1(3, MOTOR34_64KHZ);
UC_DCMotor rightMotor1(4, MOTOR34_64KHZ);
UC_DCMotor leftMotor2(1, MOTOR34_64KHZ);
UC_DCMotor rightMotor2(2, MOTOR34_64KHZ);

Servo servo;


int angle = 90;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  servo.attach(SERVO_PIN);
  servo.write(angle);
  delay(2000);
  servo.detach();
  delay(100);
}

void loop() {
  if (Serial.available() > 0) {
                // read the incoming byte:
                char serialread = Serial.read();
                unsigned char c = serialread & 0xff;
                
                if(c == 0x77){
                  moveForward();
                }
                else if(c == 0x73){
                  moveBackward();
                }
                else if(c == 0x61){
                  moveLeft();
                }
                else if(c == 0x64){
                  moveRight();
                }
                else if(c == 0x71){
                  moveServoLeft();
                }
                else if(c == 0x65){
                  moveServoRight();
                }
        }
}
void moveForward() {
        leftMotor1.run(0x01); rightMotor1.run(0x01);
        leftMotor2.run(0x01); rightMotor2.run(0x01);
        leftMotor1.setSpeed(200); rightMotor1.setSpeed(200);
        leftMotor2.setSpeed(200); rightMotor2.setSpeed(200);
        delay(1000);
        leftMotor1.setSpeed(00); rightMotor1.setSpeed(00);
        leftMotor2.setSpeed(00); rightMotor2.setSpeed(00);
        delay(500);
}


void moveBackward(){
        leftMotor1.run(0x02); rightMotor1.run(0x02);
        leftMotor2.run(0x02); rightMotor2.run(0x02);
        leftMotor1.setSpeed(200); rightMotor1.setSpeed(200);
        leftMotor2.setSpeed(200); rightMotor2.setSpeed(200);
        delay(1000);
        leftMotor1.setSpeed(00); rightMotor1.setSpeed(00);
        leftMotor2.setSpeed(00); rightMotor2.setSpeed(00);
        delay(500);
}

void moveLeft(){
        leftMotor1.run(0x03); rightMotor1.run(0x03);
        leftMotor2.run(0x03); rightMotor2.run(0x03);
        leftMotor1.setSpeed(200); rightMotor1.setSpeed(200);
        leftMotor2.setSpeed(200); rightMotor2.setSpeed(200);
        delay(500); 
        leftMotor1.setSpeed(00); rightMotor1.setSpeed(00);
        leftMotor2.setSpeed(00); rightMotor2.setSpeed(00);
        delay(1000);
}

void moveRight(){  
        leftMotor1.run(0x04); rightMotor1.run(0x04);
        leftMotor2.run(0x04); rightMotor2.run(0x04);
        leftMotor1.setSpeed(200); rightMotor1.setSpeed(200);
        leftMotor2.setSpeed(200); rightMotor2.setSpeed(200);
        delay(500);      
        leftMotor1.setSpeed(00); rightMotor1.setSpeed(00);
        leftMotor2.setSpeed(00); rightMotor2.setSpeed(00);
        delay(1000);
}

void moveServoLeft(){
  angle += 30;
  servo.attach(SERVO_PIN);
  servo.write(angle);
  delay(300);
  servo.detach();
}
void moveServoRight(){
  angle -= 30;
  servo.attach(SERVO_PIN);
  servo.write(angle);
  delay(300);
  servo.detach();
}
