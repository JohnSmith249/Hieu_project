//Jagjot Singh Sandhu//
char b;
char c ='0';
char d ='1';
void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  while (Serial.available())
  {
     b = Serial.read();
     if (b ==  c){
     digitalWrite(13,LOW);
     }
     else if (b == d) {
      digitalWrite(13,HIGH);
     }
    
  }
  
}
