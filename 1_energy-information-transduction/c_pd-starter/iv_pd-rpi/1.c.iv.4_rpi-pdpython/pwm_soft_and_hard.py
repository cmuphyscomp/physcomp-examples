#!/usr/bin/env python
# pwm_soft_and_hard.py : trivial demonstration of using GPIO pins using wiringPi on a Raspberry Pi

import os
import wiringpi2 as wp

################################################################
# script to invoke when called from command line
if __name__ == "__main__":

    if os.geteuid() != 0:
        print "Sorry, this script must be run as root, try prepending sudo."
        exit(1)

    # Use the BroadCom GPIO pin numbering scheme.
    wp.wiringPiSetupGpio()

    # Set BCM 18/Physical 12/WPi 1 to hardware PWM mode.
    wp.pinMode( 18, wp.GPIO.PWM_OUTPUT )
    wp.pwmWrite( 18, 512 ) # square wave

    # Set BCM 23/Physical 16/WPi 4 to digital output mode for 'soft' PWM.
    wp.pinMode( 23, wp.GPIO.OUTPUT )

    # Toggle as fast as possible.
    print "Entering loop to toggle physical pin 16 as fast as possible. Control-C to exit."
    while True:
        wp.digitalWrite( 23, 0 )
        wp.digitalWrite( 23, 1 )
