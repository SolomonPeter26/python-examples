#------------------------------------------------------------------------------
#           Name: string_to_array.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to modify a string by
#                 converting it to an array
#------------------------------------------------------------------------------

import array

str = 'My name is Kevin'

print( 'str = ' + str )

# We're not allowed to modify strings so we'll need to convert it to a
# character array instead...

charArray        = array.array( 'B', str )     # assignment
charArray[11:16] = array.array( 'B', 'Jason' ) # replacement

str = charArray.tostring() # assignment back to the string object

print( 'str = ' + str )

input( '\n\nPress Enter to exit...' )
