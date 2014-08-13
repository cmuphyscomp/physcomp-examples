#define DIR_PIN 2
#define STEP_PIN 3

int previous = 0;

void setup() { 
  pinMode(DIR_PIN, OUTPUT); 
  pinMode(STEP_PIN, OUTPUT); 
} 

void loop(){ 
  int val = analogRead(0);
  rotate(val - previous, .2); 
  previous = val;
}


void rotate(float dist, float speed){ 
  //rotate a specific distance (negitive for reverse movement)
  //speed is any number from .01 -> 1 with 1 being fastest - Slower is stronger
  int dir = (dist > 0)? HIGH:LOW;
  digitalWrite(DIR_PIN,dir); 

  int steps = abs(dist)*(1/0.225);
  float usDelay = (1/speed) * 70;

  for(int i=0; i < steps; i++){ 
    digitalWrite(STEP_PIN, HIGH); 
    delayMicroseconds(usDelay); 

    digitalWrite(STEP_PIN, LOW); 
    delayMicroseconds(usDelay); 
  } 
}

