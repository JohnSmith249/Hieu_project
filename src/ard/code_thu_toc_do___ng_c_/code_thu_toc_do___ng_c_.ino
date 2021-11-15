#define DIR_X 5
#define DIR_Y 6
//#define DIR_Z 7

#define STEP_X 2
#define STEP_Y 3
//#define STEP_Z 4

#define ENABLE_PIN 8

void setup() {
  Serial.begin(9600);
  pinMode(DIR_X, OUTPUT);
  pinMode(STEP_X, OUTPUT);
  pinMode(DIR_Y, OUTPUT);
  pinMode(STEP_Y, OUTPUT);
  pinMode(ENABLE_PIN, OUTPUT);
  digitalWrite(DIR_X, HIGH);
  digitalWrite(DIR_Y, HIGH);
  digitalWrite(ENABLE_PIN, LOW);
}

void loop() {
  while (Serial.available() == 0);
  int sig = Serial.read() - '0';
  if (sig == 1) {
    int Speed_X = 600;
    digitalWrite(DIR_X, HIGH);
    digitalWrite(DIR_Y, HIGH);
    boolean flag = 0;
    while (Speed_X < 1200) {
      if (flag == 0) {
        digitalWrite(DIR_X, HIGH);
        flag = 1;
      } else {
        digitalWrite(DIR_X, LOW);
        flag = 0;
      }
      for (int i = 0; i < 500; i++) {
        digitalWrite(STEP_X, HIGH);
        delayMicroseconds(Speed_X);
        digitalWrite(STEP_X, LOW);
        delayMicroseconds(Speed_X);
      }
      Speed_X += 5;
      Serial.println(Speed_X);
      delay(100);
    }
  }
}
