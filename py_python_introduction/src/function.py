#------------------------------------------------------------------------------
#           Name: function.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to create a function
#                 that writes the Fibonacci series up to n.
#------------------------------------------------------------------------------

def fibonacci( n ):
    a, b = 0, 1
    while b < n:
        print( b )
        a, b = b, a+b

# Now call the function we just defined...

fibonacci( 2000 )

input( '\n\nPress Enter to exit...' )
