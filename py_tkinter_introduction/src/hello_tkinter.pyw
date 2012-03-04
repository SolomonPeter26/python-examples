#------------------------------------------------------------------------------
#           Name: hello_tkinter.pyw
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python script demonstrates the simplest Tkinter program
#                 that I could think of.
#
# NOTE: To prevent a console from popping up when a Tkinter based window is
# executed, this script uses the .pyw extension. If you want to modify this
# script and need to output debugging information, change the extension back
# to .py.
#------------------------------------------------------------------------------

from tkinter import *

# Create the root window using Tkinter
root = Tk()
root.title( "Hello!" )
root.geometry( "200x100" )

# Create a frame in the window to hold other widgets
myFrame = Frame( root )
myFrame.grid()

# Create a label in the frame
myLabel = Label( myFrame, text = "Hello from Tkinter!" )
myLabel.grid()

# Start the window's event loop
root.mainloop()
