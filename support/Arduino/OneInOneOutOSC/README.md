OneInOneOutOSC Arduino Sketch
=============================

This example is intended as a starting point for adding low-latency
hardware-level computing on an Arduino coupled to dynamic code (e.g. Pure Data
or Python) on a laptop or Raspberry Pi.  The communications between the Arduino
and the host uses the OSC protocol ("Open Sound Control") over a USB serial
port.

OSC is an extensible message-based protocol.  The particular OSC message scheme
implemented in this sketch is similar to the SerialOscuino scheme, but
simplified for clarity.

Please see the comments in the code for more details on the messaging scheme.

Installation
------------

This sketch assumes that the CNMAT OSC Arduino library has already been
installed in your Arduino IDE.

The library is available at [github](https://github.com/CNMAT/OSC).  The most
general way to obtain the library is to *clone* the library using git from [the
library master branch](https://github.com/CNMAT/OSC.git), as this would allow
updating your installation to incorporate upstream changes.  Alternatively you
can [download a zip file of the current library
version](https://github.com/CNMAT/OSC/archive/master.zip).  More [help on git
can be found at github](https://help.github.com/articles/set-up-git).

Libraries are installed in the Arduino IDE by copying them to the libraries/
subfolder of your sketch folder.  If you have a library in a zip file, this can
be done via the Sketch/Import Library/Add Library menu.  If you have a regular
folder of files, it can simply be manually moved into the libraries/ folder.
The [Arduino tutorial on library installation can be found at the main Arduino
site](http://arduino.cc/en/Guide/Libraries).

Once the library is installed, the sketch can be compiled and downloaded as usual
to the Arduino.  Be sure to note the serial port name, as that will need to be
supplied to the code on the host.  The name can be seen and selected on the
Tools/Port menu.

Reference
---------

  [OSC on Wikipedia](http://en.wikipedia.org/wiki/Open_Sound_Control)
  [OSC home] (http://opensoundcontrol.org/)

Open Sound Control is an open protocol implemented by many commercial and
open-source systems.  It is most commonly used to transport messages over an IP
network rather than a serial port.  Specific applications such as [touch-based
user interfaces](http://www.tuio.org/) define specific message naming schemes to
be carried within the OSC protocol.

