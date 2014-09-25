# short test script for testing the Python clients object outside of Pd

import clients

if __name__ == "__main__":
    obj = clients.ClientTable()

    # approximately simulate a connection transaction
    print "address", obj.pack_address( 192, 168, 2, 3 )

    # instrument 1 connects
    print "hello:", obj.hello( 'student1', '192.168.2.3' )
    print "connect_status", obj.connect_status( 0, 1 )
    print "vote:", obj.vote( 42, '192.168.2.3' )

    # instrument 2 connects
    print "hello:", obj.hello( 'student2', '192.168.2.4' )
    print "connect_status", obj.connect_status( 1, 1 )
    print "vote:", obj.vote( 55, '192.168.2.4' )

    # instrument 1 disconnects
    print "goodbye:", obj.goodbye( '192.168.2.3' )
    print "connect_status", obj.connect_status( 0, 0 )

    # conductor disconnects instrument 2
    print "connect_status", obj.connect_status( 1, 0 )
