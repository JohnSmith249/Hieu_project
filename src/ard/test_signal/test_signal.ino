
void setup() {
  Serial.begin(9600);
}
int counter = 0;
void loop() {
  /*
       if (Serial.available() > 0) {
    String serialData = Serial.readStringUntil('\n');
    //    Serial.println(serialData);
    if (serialData == "123 123 123") {
      Serial.println('1');
    }
    if (serialData == "start") {
      Serial.println("start");
    }
    if (serialData == "end") {
      Serial.println("end");
    }
    }
    counter++;
  */
  String TestString = "I Love You";
  char TextContainer[10];
  TestString.toCharArray(TextContainer, 11);
  for (int i = 0; i < 10; i++) {
    Serial.println(TextContainer[i]);
  }
  while (true);
}
