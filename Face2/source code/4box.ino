#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;
Servo s4;

char serialData;

void setup() 
{
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  s1.attach(5);
  s2.attach(6);
  s3.attach(9);
  s4.attach(10);
  Serial.begin(9600);
}

void loop() 
{
  if(Serial.available() > 0)
  {
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData == 'Q'){
      digitalWrite(2,LOW);
      digitalWrite(3,HIGH);
      digitalWrite(4,LOW);
      digitalWrite(7,HIGH);
      digitalWrite(8,LOW);
      digitalWrite(11,HIGH);
      digitalWrite(12,LOW);
      digitalWrite(13,HIGH);
      s1.write(20);
      s2.write(20);
      s3.write(20);
      s4.write(20);//全部艙門開啟
    }
    else if(serialData == 'W'){
      digitalWrite(2,HIGH);
      digitalWrite(3,LOW);
      digitalWrite(4,HIGH);
      digitalWrite(7,LOW);
      digitalWrite(8,HIGH);
      digitalWrite(11,LOW);
      digitalWrite(12,HIGH);
      digitalWrite(13,LOW);
      s1.write(120);
      s2.write(120);
      s3.write(130);
      s4.write(120);//全部艙門關閉
    } 
    else if(serialData == 'A'){
      digitalWrite(2,LOW);
      digitalWrite(3,HIGH);
      s1.write(20);//第一艙門開啟
    }
    else if(serialData == 'Z'){
      digitalWrite(2,HIGH);
      digitalWrite(3,LOW);
      s1.write(120);//第一艙門關閉
    }
    else if(serialData == 'S'){
      digitalWrite(4,LOW);
      digitalWrite(7,HIGH);
      s2.write(20);//第二艙門開啟
    }
    else if(serialData == 'X'){
      digitalWrite(4,HIGH);
      digitalWrite(7,LOW);
      s2.write(120);//第二艙門關閉
    }
    else if(serialData == 'D'){
      digitalWrite(8,LOW);
      digitalWrite(11,HIGH);
      s3.write(20);//第三艙門開啟
    }
    else if(serialData == 'C'){
      digitalWrite(8,HIGH);
      digitalWrite(11,LOW);
      s3.write(130);//第三艙門關閉
    }
    else if(serialData == 'F'){
      digitalWrite(12,LOW);
      digitalWrite(13,HIGH);
      s4.write(20);//第四艙門開啟
    }
    else if(serialData == 'V'){
      digitalWrite(12,HIGH);
      digitalWrite(13,LOW);
      s4.write(120);//第四艙門關閉
    }
     
  }
}
