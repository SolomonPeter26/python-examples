#------------------------------------------------------------------------------
#           Name: string_replace.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to 
#------------------------------------------------------------------------------

str = 'one two three four'

print( "Before: " + str )

str = str.replace( 'one', '1' )
str = str.replace( 'two', '2' )
str = str.replace( 'three', '3' )
str = str.replace( 'four', '4' )

print( "After: " +  str )

input( '\n\nPress Enter to exit...' )
