#------------------------------------------------------------------------------
#           Name: sleep.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to use the sleep()
#                 function.
#------------------------------------------------------------------------------

from time import sleep

print( "We'll start off by sleeping 5 seconds" )

sleep( 5 )

print( "Ok, time to wake up!" )

wait_time = int( input( "How much longer would you like to sleep? " ) )

while wait_time > 0:
    print( "Ok, we'll sleep for " + str(wait_time) + " more seconds..." )
    sleep( wait_time )
    wait_time = int( input( "How much longer would you like to sleep? " ) )

print( "We're done!" )
