#include <Wire.h>
//#include <Servo.h>

#define Addr 0x4C
//Servo myservo;
//int grab = 2;
//int hold = 3;
//int pos = 0;

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(115200);  
  Wire.beginTransmission(Addr);
  Wire.write(0x07);
  Wire.write(0x01);
  Wire.endTransmission();

  Wire.beginTransmission(Addr);
  Wire.write(0x08);
  Wire.write(0x07);
  Wire.endTransmission();
  delay(300);
  
//  myservo.attach(1);
//  pinMode(grab,INPUT);
//  pinMode(hold,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
   unsigned int data[3];

//  grab_sig = digitalRead(grab);
//  hold_sig = digitalRead(hold);
  
  // Start I2C Transmission
  Wire.beginTransmission(Addr);
  // Select Data Register
  Wire.write(0x00);
  // Stop I2C Transmission
  Wire.endTransmission();
    
  // Request 3 bytes of data
  Wire.requestFrom(Addr, 3);
  
  // Read the three bytes 
  // xAccl, yAccl, zAccl
  if(Wire.available() == 3) 
  {
    data[0] = Wire.read();
    data[1] = Wire.read();
    data[2] = Wire.read();
  }  

  // Convert the data to 6-bits
  int xAccl = data[0] & 0x3F;
  if(xAccl > 31)
  {
    xAccl -= 64;
  }
  int yAccl = data[1] & 0x3F; 
  if(yAccl > 31)
  {
    yAccl -= 64;
  }
  int zAccl = data[2] & 0x3F;  
  if(zAccl > 31)
  {
    zAccl -= 64;
  }
  
//  if (grab_sig == HIGH) {
//    for (pos = 0; pos <= 45; pos += 1) { // goes from 0 degrees to 180 degrees
//      // in steps of 1 degree
//      myservo.write(pos);              // tell servo to go to position in variable 'pos'
//      delay(15);                       // waits 15ms for the servo to reach the position
//  }
//    digitalWrite(grab_sig,LOW);
//  }
//  if (hold_sig == HIGH) { {
//    for (pos = 45; pos >= 90; pos -= 1) { // goes from 180 degrees to 0 degrees
//      myservo.write(pos);              // tell servo to go to position in variable 'pos'
//      delay(15);                       // waits 15ms for the servo to reach the position
//    }
//    digitalWrite(hold_sig, LOW);
//  }
  
    
  // Output data to serial monitor
  Serial.print(xAccl);
  Serial.print(",");
  Serial.print(yAccl);
  Serial.print(",");
  Serial.print(zAccl);
  Serial.println("");
  //delay(1000); 
}
