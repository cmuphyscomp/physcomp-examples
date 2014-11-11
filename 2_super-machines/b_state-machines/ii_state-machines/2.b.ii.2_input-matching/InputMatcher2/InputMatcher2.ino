// InputMatcher2.ino : Arduino program to demonstrate a simple finite state machine program structure.

// Copyright (c) 2014, Garth Zeglin.  All rights reserved. Licensed under the terms
// of the BSD 3-clause license as included in LICENSE.

// The baud rate is the number of bits per second transmitted over the serial port.
#define BAUD_RATE 115200

#define INPUT_PIN 4

// Some version of the Arduino IDE don't correctly define this symbol for an
// Arduino Uno.
#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif

// Define the name for each state, and an index variable to represent the
// current state.
enum state_name_t { START = 0, STATE1, STATE2, STATE3 } state_index;

/****************************************************************/
/**** Standard entry points for Arduino system ******************/
/****************************************************************/

// Standard Arduino initialization function to configure the system.

void setup()
{
  // initialize the Serial port
  Serial.begin( BAUD_RATE );

  // configure our trivial inputs
  pinMode( INPUT_PIN, INPUT );
  pinMode( LED_BUILTIN, OUTPUT );

  // initialize the state machine
  state_index = START;
}

/****************************************************************/
// Standard Arduino polling function.

// This demonstrates a conventional switch-case structure for representing a
// finite state machine as an Arduino program.  The current state is represented
// as the value of the state_index variable.  Note that this structure allows
// for easily evaluating other subroutines or state machines concurrently with
// this one, as the execution passes through the loop() function on each
// iteration.

void loop()
{
  // select the code block corresponding to the state to generate the appropriate outputs for the state
  switch( state_index) {

  case START:
    Serial.println("Entering start state.");
    digitalWrite(LED_BUILTIN, LOW);
    break;

  case STATE1:
    Serial.println("Entering state 1.");    
    digitalWrite(LED_BUILTIN, LOW);
    break;

  case STATE2:
    Serial.println("Entering state 2.");    
    digitalWrite(LED_BUILTIN, LOW);
    break;

  case STATE3:
    Serial.println("Entering state 3.");
    digitalWrite(LED_BUILTIN, HIGH);
    break;
  }

  delay(1000);
  Serial.println("Sampling input.");
  int input = digitalRead( INPUT_PIN );

  // select the code block corresponding to the current state to evaluate the next input
  switch( state_index) {

  case START:
    if (input) state_index = STATE1;
    else state_index = START;
    break;

  case STATE1:
    if (input) state_index = START;
    else state_index = STATE2;
    break;

  case STATE2:
    if (input) state_index = STATE3;
    else state_index = STATE1;
    break;

  case STATE3:
    if (input) state_index = STATE3;
    else state_index = START;
    break;
  }
}    

/****************************************************************/

