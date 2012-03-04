#------------------------------------------------------------------------------
#           Name: socket_test_client.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to create a socket,
#                 which sends out a UDP packet every 2 seconds.
#
#                 Note, for anything to occur, you need to run this script
#                 simultaneously with the server-side script named,
#                 "socket_test_server.py".
#------------------------------------------------------------------------------

from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep, gmtime, strftime

# Since this is just a test, we'll just assume that the server will be
# running on the same machine and listening on port 5000.

SERVER_IP   = '127.0.0.1' # loop-back address
PORT_NUMBER = 5000

print "Test client sending packets to IP %s, via port %d\n" % \
      (SERVER_IP, PORT_NUMBER)

print "If you haven't started the server script already, do it now.\n"

mySocket = socket( AF_INET, SOCK_DGRAM )

while 1:
    localTime = strftime( "%H:%M:%S", gmtime() )
    mySocket.sendto( "packet_time = " + localTime, (SERVER_IP, PORT_NUMBER) )
    print "Sending packet... " + localTime
    sleep( 2 )
