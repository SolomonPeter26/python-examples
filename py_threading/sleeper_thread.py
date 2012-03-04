#------------------------------------------------------------------------------
#           Name: sleeper_thread.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to use the threading 
#                 module to create a thread that sleeps for some time, prints 
#                 a mesage, and then exits.
#------------------------------------------------------------------------------

import threading
import time

def sleepFunction( msg, seconds ):
    time.sleep( seconds )
    print msg

thread1 = threading.Thread( target=sleepFunction, args=( "4 second thread done!", 4) )
thread1.start()

thread2 = threading.Thread( target=sleepFunction, args=( "2 second thread done!", 2) )
thread2.start()

raw_input( "Waiting for threads to exit.\n\n" )
