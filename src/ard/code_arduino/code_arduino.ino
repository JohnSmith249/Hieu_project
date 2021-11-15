#include<TimerOne.h>
#include <TimerThree.h>
#include <TimerFour.h>

const int stepPin1 = 22; 
const int dirPin1 = 9; 
const int enPin1 = 24;

const int stepPin2 =28 ; 
const int dirPin2 = 3; 
const int enPin2 = 26;

const int stepPin3 = 32; 
const int dirPin3 = 4; 
const int enPin3 = 30;    

float x1, y1, z1, x2, y2, z2, x3, y3, z3;
float vtmm1 , vtmm2 , vtmm3;
int a=0, b=0, c=0;
float vt1=0.0, vt2=0.0, vt3=0.0;
int flag;
String buf_s,value;
String v1,v2,v3,v4,v5,v6,v7,symbol;
void setup()
{
//   Sets the two pins as Outputs
  Serial.begin(9600);
  vtmm1=0;
  vtmm2=0;
  vtmm3=0;
  
  pinMode(stepPin1,OUTPUT); 
  pinMode(dirPin1,OUTPUT);
  pinMode(enPin1,OUTPUT);
  digitalWrite(enPin1,LOW);

  pinMode(stepPin2,OUTPUT); 
  pinMode(dirPin2,OUTPUT);
  pinMode(enPin2,OUTPUT);
  digitalWrite(enPin2,LOW);

  pinMode(stepPin3,OUTPUT); 
  pinMode(dirPin3,OUTPUT);
  pinMode(enPin3,OUTPUT);
  digitalWrite(enPin3,LOW);

}
void step1()
{ 
  if(vtmm1>0)
   {
    digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction 
    if(a<vtmm1)
    {
      digitalWrite(stepPin1,!digitalRead(stepPin1));
      a++;
      vt1++;
    }
   }
  else
   {
    digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction 
    if(a<abs(vtmm1))
    {
      digitalWrite(stepPin1,!digitalRead(stepPin1));
      a++;
      vt1--;
    }
   }
}

void step2()
{ 
  if(vtmm2>0)
   {
    digitalWrite(dirPin2,LOW); // Enables the motor to move in a particular direction 
    if(b<vtmm2)
    {
      digitalWrite(stepPin2,!digitalRead(stepPin2));
      b++;
      vt2++;
    }
   }
  else
   {
    digitalWrite(dirPin2,HIGH); // Enables the motor to move in a particular direction 
    if(b<abs(vtmm2))
    {
      digitalWrite(stepPin2,!digitalRead(stepPin2));
      b++;
      vt2--;
    }
   }
}
void step3()
{ 
  if(vtmm3>0)
   {
    digitalWrite(dirPin3,LOW); // Enables the motor to move in a particular direction 
    if(c<vtmm3)
    {
      digitalWrite(stepPin3,!digitalRead(stepPin3));
      c++;
      vt3++;
    }
   }
  else
   {
    digitalWrite(dirPin3,HIGH); // Enables the motor to move in a particular direction 
    if(c<abs(vtmm3))
    {
      digitalWrite(stepPin3,!digitalRead(stepPin3));
      c++;
      vt3--;
    }
   }
}
void serialEvent()
{
  // nhận giá trị từ serial
  String inString = "";    // string to hold input
  int lengthString, k[3];
  int i,j;
    j=0;
    if (Serial.available() > 0) {  
    //int inByte = Serial.read();
    inString = Serial.readStringUntil('\n');// nhận chuỗi về
    lengthString = inString.length();
    for (i = 0; i < inString.length(); i++)
    {
       symbol = inString.charAt(i);
       if(symbol.equals(" ") == true)
       {
       k[j]=i;
       j++;
       }
    } 
    v1 = inString.substring(0,k[0]);
    v2 = inString.substring(k[0],k[1]);
    v3 = inString.substring(k[1],lengthString);

    y1 = v1.toFloat();
    y2 = v2.toFloat();
    y3 = v3.toFloat();
   // số xung cần cho step
   z1=y1*2.2222*2;
   z2=y2*2.2222*6;
   z3=y3*2.2222*6;
   // góc của mỗi khớp
   vtmm1=z1-vt1;
   vtmm2=z2-vt2;
   vtmm3=z3-vt3;

   a=0; b=0; c=0;
   // đồng tốc độ các step
   float e1,e2,e3;
   float vmax = max(max(abs(vtmm1),abs(vtmm2/3)),abs(vtmm3/3));
   if (vtmm1 == 0) e1 = 1000;
   else e1 = round(abs(vmax/vtmm1)*5000);
   if (vtmm2 == 0) e2 = 1000;
   else e2 = round(abs(vmax/(vtmm2/3))*(5000/3));
   if (vtmm3 == 0) e3 = 1000;
   else e3 = round(abs(vmax/(vtmm3/3))*(5000/3));

   Timer1.initialize(e1);
   Timer1.attachInterrupt(step1);
   Timer3.initialize(e2);
   Timer3.attachInterrupt(step2);
   Timer4.initialize(e3);
   Timer4.attachInterrupt(step3);
  }
}
void loop()
{
   serialEvent();
  
   value=" ";
   delay(100);
    
}
