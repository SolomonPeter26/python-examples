#------------------------------------------------------------------------------
#           Name: radio_button_response.pyw
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python script demonstrates how to create radio buttons.
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
        # Create a string variable to bind these three radio buttons
        # together as a group.
        self.current_selection = StringVar()
        
        # Create radio button #1
        self.rbttn1 = Radiobutton( self )
        self.rbttn1["text"]     = "Radio Button #1"
        self.rbttn1["variable"] = self.current_selection,
        self.rbttn1["value"]    = "radio_button_1",
        self.rbttn1["command"]  = self.update_text
        self.rbttn1.grid( row = 2, column = 0, sticky = W )
        
        # Create radio button #2
        self.rbttn2 = Radiobutton( self )
        self.rbttn2["text"]     = "Radio Button #2"
        self.rbttn2["variable"] = self.current_selection,
        self.rbttn2["value"]    = "radio_button_2",
        self.rbttn2["command"]  = self.update_text
        self.rbttn2.grid( row = 3, column = 0, sticky = W )

        # Create radio button #3
        self.rbttn3 = Radiobutton( self )
        self.rbttn3["text"]     = "Radio Button #3"
        self.rbttn3["variable"] = self.current_selection,
        self.rbttn3["value"]    = "radio_button_3",
        self.rbttn3["command"]  = self.update_text
        self.rbttn3.grid( row = 4, column = 0, sticky = W )

        # Create a text field to display the current selection
        self.selection_text = Text(self, width = 40, height = 5, wrap = WORD)
        self.selection_text.grid(row = 5, column = 0, columnspan = 3)

    def update_text( self ):
        text = "Current selection is "
        text += self.current_selection.get()
        self.selection_text.delete( 0.0, END )
        self.selection_text.insert( 0.0, text )
        
#------------------------------------------------------------------------------
# Script entry point...
#------------------------------------------------------------------------------

if __name__ == '__main__':

    root = Tk()
    root.title("Radio Buttons Sample")
    root.geometry( "200x100" )
    app = Application(root)
    root.mainloop()
