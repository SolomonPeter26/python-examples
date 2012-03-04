#------------------------------------------------------------------------------
#           Name: button_response.pyw
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python script demonstrates how to respond to button
#                 presses.
#
# NOTE: To prevent a console from popping up when a Tkinter based window is
# executed, this script uses the .pyw extension. If you want to modify this
# script and need to output debugging information, change the extension back
# to .py.
#------------------------------------------------------------------------------

import tkinter
import tkinter.messagebox

class Application( tkinter.Frame ):

    def __init__( self, master ):
        tkinter.Frame.__init__( self, master )
        self.grid()
        self.create_widget()

    def create_widget( self ):
        self.bttn = tkinter.Button( self )
        self.bttn["text"]= "Click Me!"
        self.bttn["command"] = self.respond_to_click
        self.bttn.grid()

    def respond_to_click( self ):
        tkinter.messagebox.showinfo( title = "Response", message = "You Clicked Me!" )

#------------------------------------------------------------------------------
# Script entry point...
#------------------------------------------------------------------------------

if __name__ == '__main__':

    root = tkinter.Tk()
    root.title( "Button Response" )
    root.geometry( "200x100" )
    myApp = Application(root)
    root.mainloop()
