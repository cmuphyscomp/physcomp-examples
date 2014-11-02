// -*- mode:c++; -*-
/// @file WS2801_test.ino
/// 
/// @brief Example for driving several WS2801 RGB LED modules over SPI on an Arduino UNO.
///
/// @author Garth Zeglin
/// @date 2014-09-13
///
/// @remarks The WS2801 LED driver has three current controlled LED outputs with
/// 8-bit precision (256 levels).  It is controlled over SPI by sending 24 bits
/// of pixel data at up to 25MHz rate.  Additional data is then relayed to the output
/// SPI pins to feed daisy-chained drivers.  Once the bus is quiescent for 500
/// microseconds, the data is applied to the outputs and the chip is ready to
/// receive more values.
///
/// So a large number of of drivers can be fed on each channel, limited only by
/// the overall refresh rate.  But the data must be fed without interruption to
/// avoid prematurely ending the cycle.
///
/// The actual color data sequence depends upon the wiring of the module; on one
/// particular strip light tested the actual sequence was blue-red-green.
///
/// Note that the relay scheme means that first three bytes output feed the
/// first module, the second three the second module, etc.  In other words, the
/// strand is not a shift register.  Extra data has no effect.

/// This sketch assumes the following electrical connections from the Arduino to
/// the first module in a chain:

/// PIN11 (MOSI)  ->  DAT
/// PIN13 (SCK)   ->  CLK
/// GND           ->  GND

// Include the SPI library.
#include <SPI.h>


void setup() 
{
  SPI.begin();  // initialize SPI hardware
}

void loop() 
{
  static int cycle = 0;

  // on each iteration, shift out RGB data for several pixels, then delay to allow the device to update.
  for (int pixel = 0; pixel < 3; pixel++ ) {
    uint8_t red   =  3 * (cycle + 32*pixel);
    uint8_t green =  5 * (cycle + 32*pixel);
    uint8_t blue  =  7 * (cycle + 32*pixel);
    SPI.transfer( blue  );
    SPI.transfer( red   );
    SPI.transfer( green );
  }
  
  delay(1);  // delay 1 millisecond to allow outputs to update
  cycle++;   // update the overall animation

  // add a delay to control the overall frame rate
  delay(20); 
}
