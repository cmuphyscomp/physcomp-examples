// OneInOneOutOSC.ino : Arduino program to act as an simplified hardware I/O server using OSC.

// Copyright (c) 2014, Garth Zeglin.  All rights reserved. Licensed under the terms
// of the BSD 3-clause license as included in LICENSE.

// This example is intended as a starting point for adding low-latency
// hardware-level computing on an Arduino coupled to dynamic code (e.g. Pd) on a
// laptop or Raspberry Pi.  The communications between the Arduino and the host
// uses the OSC protocol ("Open Sound Control").  This is an extensible
// message-based protocol.  The particular OSC message scheme is similar to the
// SerialOscuino scheme, but simplified for clarity.

// This sketch currently works on an Arduino Due but *not* on an Arduino Uno
// due to limitations of the OSC library.

/****************************************************************/
/**** OSC addressing scheme *************************************/
/****************************************************************/

// OSC is 'Open Sound Control', a lightweight protocol for communicating event
// data over a network or serial channel.  In practice, an application using OSC
// needs to define a specific protocol of addresses and message formats.

// OSC messages are each addressed to a specific channel designated by a string
// of tokens separated by slashes.  Each message can contain multiple values,
// each of which can be a number (integer or float) or a string.  The address
// scheme is interpreted by the program receiving the message and can be
// different in each direction.

// In the following scheme, <number> represents a value which can be either
// integer or floating point.

// The following messages are recognized by this program:

// Address      Values			Meaning
//   /s/l	<integer>		controls the built-in LED, value is 0 or non-zero
//   /a/2	<number>		PWM control on PWM2, value is 0 to 1
//   /d/3	<number>		digital output on PIN3, value is 0 or non-zero
//   /servo/4   <number>                hobby servo PWM control signal on PIN4, value is 0 to 180 (angle in degrees)

// This program generates the following messages:

// Address      Values			Meaning
//   /s/db	<string>		debugging message to print for user
//   /s/db	<integer>		numeric value to print for debugging
//   /s/m	<integer>		Arduino clock time in microseconds
//   /s/l	<integer>		reply to /s/l with current LED state
//   /a/0	<integer>		analog input value on A0, value is 0 to 1023
//   /d/8	<integer>		digital input value on PIN8, value is 0 or 1

/****************************************************************/
/**** Library imports *******************************************/
/****************************************************************/

// Import definitions from the CNMAT OSC library.  This must be installed in the
// libraries path of the Arduino sketch folder.  The library is available via
// https://github.com/CNMAT/OSC

#include <OSCMessage.h>
#include <SLIPEncodedSerial.h>

// Use the Servo library for generating control signals for hobby servomotors.
// Hobby servos require a specific form of pulse-width modulated control signal,
// usually with positive-going pulses between 1 and 2 milliseconds repeated at
// 50 Hz.  Note that this is a significantly different signal than the PWM
// usually required for powering a motor at variable torque.
#include <Servo.h>

/****************************************************************/
/**** Global variables and constants ****************************/
/****************************************************************/

// Create a wrapper around the serial port to encode and decode packets.
SLIPEncodedSerial SLIPSerial(Serial);

// The baud rate is the number of bits per second transmitted over the serial port.
const int baud_rate = 57600;  

// Interval in milliseconds between input samples.
static unsigned int hardware_polling_interval = 1000;

// Create a hobby servo control signal generator.
static Servo servo_output;
static const int servo_output_pin = 4;

/****************************************************************/
/**** Utility functions *****************************************/
/****************************************************************/

// Send an OSC message object across the serial port to the Linux host.
static void send_OSC_message( OSCMessage& msg )
{
  SLIPSerial.beginPacket();
  msg.send(SLIPSerial);
  SLIPSerial.endPacket();
}

/****************************************************************/
// Send a single debugging string to the console.
static void send_debug_message( const char *str )
{
  OSCMessage msg("/s/db");
  msg.add(str);
  send_OSC_message( msg);
}

/****************************************************************/
// Send a single debugging integer to the console.
static void send_debug_integer( int i )
{
  OSCMessage msg("/s/db");
  msg.add(i);
  send_OSC_message( msg);
}

/****************************************************************/
/**** Functions to interpret OSC messages ***********************/
/****************************************************************/

// Process the 'system' messages received in the /s namespace.
static void routeSystem(OSCMessage& msg, int addrOffset )
{
  // OSC address /s/l controls the built-in LED
  if (msg.fullMatch("/l", addrOffset)) {
    // if the first value in the message is an integer
    if (msg.isInt(0)){
      int i = msg.getInt(0);

      // Unlike the Due, the Udoo SAM3X does not have a built-in
      // LED, so on the Udoo this will just perform the reply
      // without any hardware actions.
#ifdef LED_BUILTIN
      pinMode( LED_BUILTIN, OUTPUT );
      // turn on the LED if that value is true, then echo it back as a handshake
      digitalWrite(LED_BUILTIN, (i != 0) ? HIGH : LOW);
#endif

      OSCMessage reply("/s/l");
      reply.add(i); send_OSC_message( reply );
    }
  }
}

/****************************************************************/
// Process the 'digital' messages received in the /d namespace.
static void routeDigital( OSCMessage& msg, int addrOffset )
{
  // OSC address /d/3 controls PIN3
  if (msg.fullMatch("/3", addrOffset)) {
    pinMode( 3, OUTPUT );
    // Set the digital output state from either an integer or float value.
    if (msg.isInt(0))        digitalWrite( 3, (msg.getInt(0))          ? HIGH : LOW);
    else if (msg.isFloat(0)) digitalWrite( 3, (msg.getFloat(0) != 0.0) ? HIGH : LOW);
  }
}

/****************************************************************/
// Process the 'analog' messages received in the /a namespace.
static void routeAnalog( OSCMessage& msg, int addrOffset )
{
  // OSC address /a/2 controls PWM on PIN2
  if (msg.fullMatch("/2", addrOffset)) {

    // Set the PWM output state from either an integer or float value.
    if (msg.isFloat(0))    analogWrite( 2, (int)(msg.getFloat(0)*255.0f));
    else if (msg.isInt(0)) analogWrite( 2, (msg.getInt(0) != 0) ? 0 : 1 );
  }
}

/****************************************************************/
// Process the 'servo' output messages received in the /servo namespace.
static void routeServo( OSCMessage& msg, int addrOffset )
{
  // OSC address /servo/4 controls hobby servo output on PIN4
  if (msg.fullMatch("/4", addrOffset)) {

    // The Servo object expects an angle between 0 and 180.  Set it from either
    // an integer or float value.  Note that the specific output pin was
    // configured in the setup() function.
    if (msg.isFloat(0)) servo_output.write( (int)(msg.getFloat(0)));
    else if (msg.isInt(0)) {
      int value = msg.getInt(0);
      servo_output.write( value );
      send_debug_integer( value );
    }
    else send_debug_message("servo-err");
  }
}

/****************************************************************/
// Interpret an OSC message received from the Linux host.
static void process_OSC_message( OSCMessage& message )
{
  message.route("/s", routeSystem);
  message.route("/a", routeAnalog);
  message.route("/d", routeDigital);
  message.route("/servo", routeServo);
}

/****************************************************************/
/*** Polling functions called periodically from the main loop ***/
/****************************************************************/

// Polling function to process OSC messages arriving over the serial port from
// the Linux host.

static void serial_input_poll(void)
{
  // OSC message object to collect serial input data into a message.
  static OSCMessage *input_message = NULL;
  if (input_message == NULL) input_message = new OSCMessage;

  if( !SLIPSerial.endofPacket() ) {
    int size = SLIPSerial.available();
    while(size--) {
      // read one byte and decode it into an OSC message object
      int next_char = SLIPSerial.read();
      input_message->fill( next_char );
    }
  }

  if( SLIPSerial.endofPacket() ) {
    // once a full OSC packet has been received, process the entire message object
    if(!input_message->hasError()) process_OSC_message( *input_message );
    else send_debug_message("input-err");

    delete input_message;
    input_message = NULL;
  }
}

/****************************************************************/
// Polling function to read and send specific input values at periodic
// intervals.  N.B. The timing calculation could be improved to reduce jitter.

static void hardware_input_poll(void)
{
  static unsigned long last_time = 0;
  unsigned long now = millis();

  if ((now - last_time) > hardware_polling_interval) {
    last_time = now;

    { // send A0 analog state
      OSCMessage msg("/a/0");
      msg.add( (int32_t)analogRead(0) );
      send_OSC_message( msg );
    }

    { // send PIN8 digital state
      OSCMessage msg("/d/8");
      pinMode( 8, INPUT );
      msg.add( (int32_t) digitalRead(8) );
      send_OSC_message( msg );
    }

    { // also send a time reading
      OSCMessage msg("/s/m");
      msg.add( (int32_t) micros() );
      send_OSC_message( msg );
    }
  }
}

/****************************************************************/
/**** Standard entry points for Arduino system ******************/
/****************************************************************/

// Standard Arduino initialization function to configure the system.

void setup()
{
  // initialize the SLIPSerial object wrapping the serial port
  SLIPSerial.begin( baud_rate );

  // send an OSC message as a diagnostic
  send_debug_message("wakeup");

  // set up the hobby servo control output
  servo_output.attach( servo_output_pin );

  // additional hardware configuration can go here
}

/****************************************************************/
// Standard Arduino polling function to handle all I/O and periodic processing.
// This loop should never be allowed to stall or block so that all tasks can be
// constantly serviced.

void loop()
{
  serial_input_poll();
  hardware_input_poll();

  // other polled tasks can go here
}

/****************************************************************/
/****************************************************************/
