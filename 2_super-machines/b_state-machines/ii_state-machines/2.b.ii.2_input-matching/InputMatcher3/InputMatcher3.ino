// InputMatcher3.ino : Arduino program to demonstrate a simple finite state machine program structure.

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
/****************************************************************/
// Define a table of state transitions and state outputs.

struct state_t {
  const char *name;
  int led_output;
  enum state_name_t high_transition;
  enum state_name_t low_transition;

};

struct state_t states[] = {
  { "START",  LOW,  STATE1, START  },
  { "STATE1", LOW,  START,  STATE2 },
  { "STATE2", LOW,  STATE3, STATE1 },
  { "STATE3", HIGH, STATE3, START  }
  };

/****************************************************************/
// This demonstrates a table-based approach for representing a finite state
// machine as an Arduino program.  The current state is represented as the value
// of the state_index variable.  All transitions are specified in the
// table. Note that this structure is highly extensible and allows for easily
// evaluating other subroutines or state machines concurrently with this one.
// It is effectively an extremely simple language interpreter.

void loop()
{
  // select the state table entry corresponding to the state
  struct state_t& current = states[state_index];

  // generate the appropriate outputs for the state
  Serial.print( "Entering state: " );
  Serial.println( current.name );
  digitalWrite( LED_BUILTIN, current.led_output );

  // process inputs
  delay(1000);
  Serial.println("Sampling input.");
  int input = digitalRead( INPUT_PIN );

  // choose the successor state based on the table entry
  if (input) state_index = current.high_transition;
  else       state_index = current.low_transition;
}

/****************************************************************/

