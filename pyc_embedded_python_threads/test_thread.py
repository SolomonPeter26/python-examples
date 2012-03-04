#------------------------------------------------------------------------------
#           Name: test_thread.py
#         Author: Kevin Harris
#  Last Modified: 04/29/05
#    Description: 
#------------------------------------------------------------------------------

import threadTest
import threading
import time

#------------------------------------------------------------------------------
# Define a function and set it as a call-back so the application can call 
# into this script.
#------------------------------------------------------------------------------

def myPythonFunction( n ):
    print "Main thread   - Application called myPythonFunction and passed: " + str( n )

threadTest.setCallback( myPythonFunction );

#------------------------------------------------------------------------------
# Define a function which will run in a separate Python thread.
#------------------------------------------------------------------------------

def threadFunction():
    for i in range( 100 ):
		threadTest.myCppFunction( i )
		#time.sleep( 0.1 )

myThread = threading.Thread( target=threadFunction )
myThread.start()
