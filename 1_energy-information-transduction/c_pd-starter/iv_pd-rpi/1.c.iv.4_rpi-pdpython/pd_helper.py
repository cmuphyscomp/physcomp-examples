# pd_helper.py : simple demonstration of invoking a Python object from within Pd.

import socket
import wiringpi2 as wp
import time

################################################################
# Python class to instantiate
class Helper:
    def __init__(self):
        pass

    def lookup_host( self, name ):
        return socket.gethostbyname( name )


    def init_wiringPi( self ):
        wp.wiringPiSetupGpio()
        return

    def enable_pwm_pin( self ):
        # Set BCM 18/Physical 12/WPi 1 to hardware PWM mode.
        wp.pinMode( 18, wp.GPIO.PWM_OUTPUT )
        return

    def pwm_fast_ramp( self ):
        # A somewhat contrived example, this will create 'ramp'
        # by changing the PWM output from zero to max as fast as
        # possible.
        start = time.clock()

        # modulate the PWM signal as fast as possible
        for i in range(1024):
            wp.pwmWrite( 18, i )

        # return the elapsed time
        return time.clock() - start

################################################################
# Script to invoke when called from the command line; this is
# useful for testing outside of Pd.

if __name__ == "__main__":
    helper = Helper()
    name = "www.cmu.edu"
    print "IP address for %s is %s." % (name, helper.lookup_host( name ))
