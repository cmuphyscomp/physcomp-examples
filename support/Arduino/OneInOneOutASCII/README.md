OneInOneOutASCII Arduino Sketch
===============================

This example is intended as a starting point for adding low-latency
hardware-level computing on an Arduino coupled to dynamic code (e.g. Pure Data
or Python) on a laptop or Raspberry Pi.  The communications between the Arduino
and the host uses a simple message protocol based on lines ASCII text.

The benefit of the simple message format is that the output can be read using
just the Arduino IDE Serial Monitor for ease of debugging.  The code is
self-contained, no special libraries are required.  The messaging scheme should
be fairly easy to extend to handle additional application-specific messages.

Please see the comments in the code for more details on the messaging scheme.

