#------------------------------------------------------------------------------
#           Name: socket_test_server.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to create a socket,
#                 which will act as a simple server by listening to port 5000.
#
#                 Note, for anything to occur, you need to run this script
#                 simultaneously with the client-side script named,
#                 "socket_test_client.py".
#------------------------------------------------------------------------------

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM

PORT_NUMBER = 5000

hostName = gethostbyname( 'localhost' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print "Test server listening on port %d\n" % PORT_NUMBER

print "If you haven't started one or more client scripts already, do it now.\n"

while 1:
    (data, addr) = mySocket.recvfrom( 50 ) # Just hard-code the data amount to read to 50
    print "Received packet from: " + `addr` + ", " + data

