#------------------------------------------------------------------------------
#           Name: create_buttons.pyw
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python script demonstrates the different ways in which
#                 buttons can be created.
#
# NOTE: To prevent a console from popping up when a Tkinter based window is
# executed, this script uses the .pyw extension. If you want to modify this
# script and need to output debugging information, change the extension back
# to .py.
#------------------------------------------------------------------------------

from tkinter import *

class Application( Frame ):

    def __init__( self, master ):
        Frame.__init__( self, master )
        self.grid()
        self.create_widgets()

    def create_widgets( self ):
        # Create three buttons. Note how each one is setup slightly different.
        
        # Create the first button...
        self.bttn1 = Button( self, text = "Button #1" )
        self.bttn1.grid()

        # Create the second button...
        self.bttn2 = Button( self )
        self.bttn2.grid()	
        self.bttn2.configure( text = "Button #2" )

        # Create the third button...
        self.bttn3 = Button( self )
        self.bttn3.grid()
        self.bttn3["text"] = "Button #3"

#------------------------------------------------------------------------------
# Script entry point...
#------------------------------------------------------------------------------

if __name__ == '__main__':

    root = Tk()
    root.title( "Buttons Sample" )
    root.geometry( "200x100" )
    myApp = Application( root )
    root.mainloop()
