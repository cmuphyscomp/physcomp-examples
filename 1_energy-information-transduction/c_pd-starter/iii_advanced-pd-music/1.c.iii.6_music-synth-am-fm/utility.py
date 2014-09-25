# utility.py : support functions for manipulating Pd data in convenient ways

class Utility:
    def __init__(self):
        pass

    def qlist_beats( self, beat_pattern ):
        """Given a string representing a pattern of beats, generate a tuple of outputs for configuring a qlist object."""
        
        result = list()
        tempo_interval = 250   # in milliseconds, this is a 120 bpm eighth note
        time = 0
        # iterate over the string, generating messages for the qlist object
        
        for c in beat_pattern:
            if c == 'a':
                # generate a single event configuration message for qlist
                msg = [ 'add', tempo_interval, 'i1', 64 ]
                result.append(msg)


            elif c == 'B':
                # generate a single event configuration message for qlist
                msg = [ 'add', 2*tempo_interval, 'i2', 69 ]
                result.append(msg)

        # return the result as a tuple of lists; each list will be emitted
        # separately into any attached qlist to configure its event list
        return tuple(result)

    

# If called from the command line, run debugging tests.
if __name__ == "__main__":
    
    utility = Utility()

    value = utility.qlist_beats("aBaB")
    print "qlist configuration values:", value


