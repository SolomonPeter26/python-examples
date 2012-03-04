#------------------------------------------------------------------------------
#           Name: sleeper_thread_class.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to use the threading 
#                 module to create a thread that sleeps for some time, prints 
#                 a mesage, and then exits.
#------------------------------------------------------------------------------

import threading
import time

class Sleeper( threading.Thread ):
    
    def __init__( self, msg, seconds ):
        self.msg = msg
        self.seconds = seconds
        threading.Thread.__init__(self)
        
    def run( self ):
        time.sleep( self.seconds )
        print self.msg

thread1 = Sleeper( "4 second thread done!", 4 )
thread1.start()

thread2 = Sleeper( "2 second thread done!", 2 )
thread2.start()

raw_input( "Waiting for threads to exit.\n\n" )
