
void setup() {
  Serial.begin(9600);
}
int counter = 0;
char container[3] = {};


void loop() {

  if (Serial.available() > 0) {
    counter = 0;
    String serialData = Serial.readStringUntil('\n');
    if (seriData == "start") {
      while (serialData != "end") {
        if (serialData != "start") {
          container[counter] = serialData;
          counter++;
          serialData = Serial.readStringUntil('\n');
        }
      }
    }
  }

  char String_to_char() {

  }
