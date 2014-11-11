// InputMatcher1.ino : Arduino program to demonstrate a simple finite state machine program structure.

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
}

/****************************************************************/
// Standard Arduino polling function.

// This demonstrates the simplest method for representing a finite state machine
// as an Arduino program: the program counter is used to represent the current
// state as the current execution position with the program.  Note that a
// highly-connected state graph is not necessarily well represented by a
// hierarchical code structure, hence the use of goto, which is generally
// frowned upon in structured programming.

void loop()
{
  int input;

 start:
  Serial.println("Entering start state.");
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  Serial.println("Sampling input.");
  input = digitalRead( INPUT_PIN );
  if (input) goto state1;
  else goto start;

 state1:
  Serial.println("Entering state 1.");    
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  Serial.println("Sampling input.");
  input = digitalRead( INPUT_PIN );
  if (input) goto start;
  else goto state2;

 state2:
  Serial.println("Entering state 2.");    
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  Serial.println("Sampling input.");
  input = digitalRead( INPUT_PIN );
  if (input) goto state3;
  else goto state1;

 state3:
  Serial.println("Entering state 3.");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  Serial.println("Sampling input.");
  input = digitalRead( INPUT_PIN );
  if (input) goto state3;
  else goto start;
}    

/****************************************************************/

