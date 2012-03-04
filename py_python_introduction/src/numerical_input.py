#------------------------------------------------------------------------------
#           Name: numerical_input.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to get numerical input
#                 from the command line and use the if-else conditional.
#------------------------------------------------------------------------------

print()
print( "Welcome to the Area calculation program" )
print( "---------------------------------------" )
print()

# Print out the menu:
print( "Please select a shape:" )
print( "1  Rectangle" )
print( "2  Circle" )
print()

# The input function both prompts the user for input and fetches it...
shape = int( input( "> " ) )

# Calculate the area...
if shape == 1:
    height = int( input("Please enter the height: ") )
    width = int( input("Please enter the width: ") )
    area = height*width
    print( "The area is", area )
else:
    radius = int( input("Please enter the radius: ") )
    area = 3.14*(radius**2)
    print(  "The area is", area )

input( '\n\nPress Enter to exit...' )
