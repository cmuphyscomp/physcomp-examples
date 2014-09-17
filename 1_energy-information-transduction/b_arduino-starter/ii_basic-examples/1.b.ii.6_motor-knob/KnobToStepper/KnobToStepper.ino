// KnobToStepper.ino : demonstrate operation of a stepper motor driver and mapping an analog input to a position output

// Define the pin numbers on which the outputs are generated.
#define DIR_PIN 2     // The direction pin controls the direction of stepper motor rotation.
#define STEP_PIN 3    // Each pulse on the STEP pin moves the stepper motor one angular unit.

/****************************************************************/
// This function is called once after reset to initialize the program.
void setup()
{
  // Initialize the digital output pins to output drive mode.
  pinMode(DIR_PIN, OUTPUT); 
  pinMode(STEP_PIN, OUTPUT); 
} 
/****************************************************************/
// Global variables.
int previous = 0;     // the previous analog input value

/****************************************************************/
// This function executes a stepper motor motion for a given distance and speed.
// It does not return until the motion is complete, e.g. it 'blocks' for the
// duration.
//   dist  is the angular displacement in arbitrary units (negative for reverse movement)
//   speed is a number from .01 -> 1, with 1 being fastest.

void rotate(float dist, float speed)
{
  // Configure the direction pin on the stepper motor driver based on the sign
  // of the displacement.
  int dir = (dist > 0)? HIGH:LOW;
  digitalWrite(DIR_PIN,dir); 

  // Compute an integer number of step cycles to perform using the absolute
  // value of the displacment and arbitrary scaling.
  int steps = abs(dist)*(1/0.225);

  // Compute a delay time in microseconds controlling the duration of each half
  // of the step cycle.
  float usDelay = (1/speed) * 70;

  // Loop for the given number of step cycles, producing a square wave step
  // command for the stepper motor driver.
  for(int i = 0; i < steps; i++) {
    digitalWrite(STEP_PIN, HIGH); 
    delayMicroseconds(usDelay); 

    digitalWrite(STEP_PIN, LOW); 
    delayMicroseconds(usDelay); 
  } 
}

/****************************************************************/
// This function is called repeatedly as fast as possible from within the
// built-in library to poll program events.

void loop()
{

  // read the current value of the potentiometer input from analog input 0
  int val = analogRead(0);

  // compute the displacement from the previous reading and execute a
  // proportional angular motor move at a specified speed
  rotate( val - previous, 0.2 );

  // save the last potentiometer value for the next displacement calculation
  previous = val;
}

/****************************************************************/
