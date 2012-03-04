#------------------------------------------------------------------------------
#           Name: iterators.py
#         Author: Kevin Harris
#  Last Modified: 03/11/04
#    Description: This Python script demonstrates how to use iterators.
#------------------------------------------------------------------------------

myTuple = (1, 2, 3, 4)
myIterator = iter( myTuple )

print( next( myIterator ) )
print( next( myIterator ) )
print( next( myIterator ) )
print( next( myIterator ) )

# Becareful, one more call to next() and this script will throw an exception!
#print myIterator.next() 

print( " " )

#------------------------------------------------------------------------------

# If you have no idea how many items can be safely accesd via the iterator,
# use a try/except block to keep your script from crashing.

myTuple2 = ( "one", "two", "three", "four" )
myIterator2 = iter( myTuple2 )

while 1:
    try:
        print( next( myIterator2 ) )
    except StopIteration:
        print( "Exception caught! Iterator must be empty!" )
        break

input( '\n\nPress Enter to exit...' )
