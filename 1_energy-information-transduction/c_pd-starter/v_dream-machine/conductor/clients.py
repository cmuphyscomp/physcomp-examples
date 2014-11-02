# Python object to support the conductor.pd patch for running a conductor station.

# This table manages a list of connected client and issues commands back to the
# Pd interface to display state and manage the UDP socket states.

# The interface offers a list of 'channels' each representing a UDP connection to a client.

# Pd messages recognized by the channels follow these patterns:
#  [ channel-#  {name | ip | vote } value ]                  set a GUI value
#  [ channel-# port connect ip-address port-number ]         connect to a remote instrument
#  [ channel-# port disconnect ]                             disconnect the UDP socket

#================================================================
import pdgui
import socket

# utility function to return the channel name token for a given channel number
def token( index ):
    return "channel-%d" % index

# UDP port number for the instruments; this is hard-coded in instrument.pd
INSTRUMENT_PORT = 20000

# number of channels shown in display; this is hard-coded in conductor.pd
CHANNELS = 11

#================================================================
class ClientTable:

    # static class variables to manage the client connection state

    # table of channels available in the display
    channels = [ { 'name': None, 'address': None } for n in range(CHANNELS) ]

    # mapping from address to channel number
    addresses = dict()  

    # allocate a new channel, assigning it an address, and returning the channel index, returning None if not available
    def allocate_first_unused_channel( self, username, address ):
        for i, c in enumerate(ClientTable.channels):
            if c['name'] is None:
                c['name'] = username
                c['address'] = address
                ClientTable.addresses[address] = i
                return i
        return None

    # de-allocate a channel, returning the appropriate GUI control messages
    def release_channel( self, channel_index ):
        # ignore spurious channel identifier
        if channel_index < 0 or channel_index >= len( ClientTable.channels ):
            return None

        # look up the connection record
        record = ClientTable.channels[channel_index]

        # remove the IP address from the address dictionary
        address = record['address']
        if address is not None:
            if ClientTable.addresses.has_key( address ):
                del ClientTable.addresses[address]

        # if the channel is already released, nothing more to do
        if record['name'] is None:
            return None

        else:
            # erase the record and reset the GUI
            record['name'] = None
            record['address'] = None
            n = token( channel_index  )
            return ( [ n, 'port', 'disconnect' ], [n, 'name', '-nobody-' ], [n, 'ip', '-none-' ], [n, 'vote', 0] )

    # ----------------------------------------------------------------
    # Initialize the instance of this class.  N.B. this class can be instanced
    # many times in a patch, but class variables are used so every instance
    # references the same underlying data.
    def __init__(self):
        pass

    # utility function to pack a four-part IPv4 address back into a symbol
    def pack_address( self, i1, i2, i3, i4 ):
        return "%d.%d.%d.%d" % ( i1, i2, i3, i4 )

    # utility function to return the IP address of this machine
    def this_host_ip( self ):
        # this won't work reliably with more than one network interface
        return socket.gethostbyname( socket.gethostname () )

    # ----------------------------------------------------------------
    # Messages received from the receiver object.  Each of these may return a
    # tuple of messages to broadcast on [r channel-commands] to change the Pd
    # state.

    def hello( self, name, address ):
        new_channel = self.allocate_first_unused_channel( name, address )
        if new_channel is not None:
            n = token(new_channel)
            return ( [ n, 'name', name ], [n, 'vote', 0 ], [n, 'ip', address ], [n, 'port', 'connect', address, INSTRUMENT_PORT ] )
        else:
            pdgui.post( "Channel table is full, ignoring connection request from %s at %s." % (name, address) )
            return None

    def goodbye( self, address ):
        channel_index = ClientTable.addresses[address]
        if channel_index is not None:
            return self.release_channel( channel_index )
        else:
            return None

    def vote( self, value, address ):
        n = token(0)
        return [n, 'vote', value]

    def connect_status( self, channel_index, flag ):
        if flag == 0:
            # if the UDP port indicates a disconnection, make sure the channel is released
            return self.release_channel( int(channel_index) )
        else:
            # this can just ignore connection confirmation
            return None
