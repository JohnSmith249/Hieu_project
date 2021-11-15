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

void move_by_step(int steps, boolean dir, int axis_step, int axis_dir, long int axis_speed) {
  digitalWrite(axis_dir, dir);
  for (int i = 0; i < steps; i++) {
    digitalWrite(axis_step, HIGH);
    delayMicroseconds(axis_speed);
    digitalWrite(axis_step, LOW);
    delayMicroseconds(1000);
  }
}

void move_by_coordinates(int coordinate_X, int coordinate_Y, int Speed) {
  if (coordinate_X < 0) {
    digitalWrite(DIR_X, LOW);
  } else {
    digitalWrite(DIR_X, HIGH);
  }
  if (coordinate_Y < 0) {
    digitalWrite(DIR_Y, LOW);
  } else {
    digitalWrite(DIR_Y, HIGH);
  }
  for (int i = 0; i < abs(coordinate_X); i++) {
    digitalWrite(STEP_X, HIGH);
    delayMicroseconds(Speed);
    digitalWrite(STEP_X, LOW);
    delayMicroseconds(Speed);
  }
  for (int i = 0; i < abs(coordinate_Y); i++) {
    digitalWrite(STEP_Y, HIGH);
    delayMicroseconds(Speed);
    digitalWrite(STEP_Y, LOW);
    delayMicroseconds(Speed);
  }
}

void sync_coordinates(){
  
}

void loop() {
  move_by_coordinates(200, -400, 1000);
  while(true);
  //  move_by_step(200, LOW, STEP_X, DIR_X, 500);
  //  delay(100);
  //  move_by_step(200, LOW, STEP_Y, DIR_Y, 500);
  //  delay(100);
  //  move_by_step(200, HIGH, STEP_X, DIR_X, 500);
  //  delay(100);
  //  move_by_step(200, HIGH, STEP_Y, DIR_Y, 500);
  //  delay(100);
}
