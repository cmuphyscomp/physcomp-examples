#!/usr/bin/env python
# instrument_client.py : demonstration of using txosc and Twisted to create an OSC network client.

# This communicates with a 'conductor' to create a synchronized performance system.

# references:
#   https://bitbucket.org/arjan/txosc/wiki/Home
#   https://twistedmatrix.com/trac/wiki/Documentation
#   http://twistedmatrix.com/documents/current/core/howto/time.html

import sys

# Twisted networking framework
from twisted.internet import task
from twisted.internet import reactor

# TxOSC OpenSoundControl library
from txosc import osc
from txosc import dispatch
from txosc import async

################################################################
class InstrumentApplication(object):

    def __init__(self ):
        self.delay = 1.0
        self.send_host = "127.0.0.1"
        self.send_port = 20001
        self.receive_port = 20000

        # set up the port transmitting instrument requests
        self.sender = async.DatagramClientProtocol()
        self._sender_port = reactor.listenUDP(0, self.sender)

        # set up the txosc UDP port listening to conductor status updates
        self.receiver = dispatch.Receiver()
        self._server_port = reactor.listenUDP(self.receive_port, async.DatagramServerProtocol(self.receiver))

        print("Listening on osc.udp://localhost:%s" % (self.receive_port))

        # set up the OSC message handling
        self.receiver.addCallback("/onoff",    self.onoff_handler)
        self.receiver.addCallback("/tempo",    self.tempo_handler)
        self.receiver.addCallback("/beat",     self.beat_handler)
        self.receiver.addCallback("/loudness", self.loudness_handler)
        self.receiver.addCallback("/tonic",    self.tonic_handler)   
        self.receiver.fallback = self.fallback
        
        # schedule future events
        reactor.callLater(  0.1, self._start)
        reactor.callLater( 10.0, self._stop)
        
        # schedule polling events
        self._polling_task = task.LoopingCall( self._poll )
        self._polling_task.start( 1.0 ) # call every second
        return

    ## other application functions ############################################

    def _poll( self ):
        print "updating"
        return

    def _start( self ):
        self.send_hello("student")
        return

    def _stop( self ):
        self.send_goodbye()
        reactor.stop()
        return

    ## OSC message handlers ############################################

    def onoff_handler( self, message, address):
        print "On/Off: ", message.getValues()[0]
        return

    def tempo_handler( self, message, address):
        print "Tempo: ", message.getValues()[0]
        return

    def beat_handler( self, message, address):
        print "Beat: ", message.getValues()[0]
        return

    def loudness_handler( self, message, address):
        print "Loudness: ", message.getValues()[0]
        return

    def tonic_handler( self, message, address):
        print "Tonic: ", message.getValues()[0]
        return

    def fallback(self, message, address):
        print "Unknown message %s from %s" % (message, address)
        return

    ## OSC message output ##########################################
    def send_hello( self, name ):
        self.sender.send(osc.Message("/hello", name ), (self.send_host, self.send_port))
        print("Sent /hello")
        
    def send_goodbye(self):
        self.sender.send(osc.Message("/goodbye"), (self.send_host, self.send_port))
        print("Sent /goodbye")


################################################################
if __name__ == "__main__":
    app = InstrumentApplication()
    reactor.run()

