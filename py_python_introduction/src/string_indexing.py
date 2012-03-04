#------------------------------------------------------------------------------
#           Name: string_indexing.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates the different ways of
#                 indexing string data.
#------------------------------------------------------------------------------

str = "one two three four"

char1 = str[0]      # "o"          Indexing forward, get a single char value at index position 0.   
end1  = str[8:]     # "three four" Indexing forward, get the end of the string starting at index position 8 
sub1  = str[4:7]    # "two"        Indexing forward, get a sub-string from index position 4 through 7 

char2 = str[-1]     # "e"          Indexing backwards, get the last char value
end2  = str[-4:]    # "four"       Indexing backwards, get the end of the string starting at -4
sub2  = str[-10:-5] # "three"      Indexing backwards, get a sub-string from index position -10 through -5  

print( "str = " + str )
print()
print( "char1 = " + char1 )
print( "end1  = " + end1 )
print( "sub1  = " + sub1 )
print()
print( "char2 = " + char2 )
print( "end2  = " + end2 )
print( "sub2  = " + sub2 )

input( '\nPress Enter to exit...' )
