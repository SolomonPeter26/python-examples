#------------------------------------------------------------------------------
#           Name: create_menu.pyw
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python script demonstrates how to create a Tkinter 
#                 based window with a menu.
#
# NOTE: To safely run this sample script from IDLE set usingIDLE to = 1
#
# NOTE: To prevent a console from popping up when a Tkinter based window is
# executed, this script uses the .pyw extension. If you want to modify this
# script and need to output debugging information, change the extension back
# to .py.
#------------------------------------------------------------------------------

from tkinter import *
import tkinter.messagebox

usingIDLE = 0

#------------------------------------------------------------------------------
# Name: myUserInterfaceClass
# Desc: Simple example of a Tkinter based user interface class.
#------------------------------------------------------------------------------

class myUserInterfaceClass:

    def __init__( self, master, ar, xy, flex ):

    #
    # Create a menu bar with one menu called "Test"...
    #

        menubar = Menu( master )   # Create a menu bar object 
        master.config( menu=menubar ) # Associate it with the root or parent

        mainmenu = Menu( menubar, tearoff=0 ) # Create a dropdown menu

        menubar.add_cascade( label = 'Test',    # Name of first menu
                             underline=  0,     # Keyboard shortcut = "T"
                             menu = mainmenu )  # Set the menu
                             

    #
    # On the menu bar's "Test" menu, create two selectable menu items 
    # called "Dialog and "Exit"...
    #

        mainmenu.add_command( label = 'Do Something',       # Name of first menu item
                              underline = 0,                # Keyboard shortcut = "D"
                              command = self.do_something ) # What to do when called

        mainmenu.add_command( label = 'Exit',       # Name of second menu item
                              underline = 1,        # Keyboard shortcut = "x"
                              command = self.quit ) # What to do when called

    #
    # Create the actual window or GUI...
    #

        self.frame = Toplevel( relief = 'ridge', # Window border style
                               borderwidth = 2,  # Border width
                               menu = menubar )  # Set the menu bar

        self.frame.geometry( ar + xy )            # Set its size & location

        self.frame.resizable( flex, flex )        # Allow or Disallow resizing

        if not usingIDLE: # Set window exit protocol, if needed.
            self.frame.protocol( 'WM_DELETE_WINDOW', self.quit )


    def quit( self ):
        if usingIDLE:
            self.frame.destroy()
        else:
            self.frame.quit()
            root.quit()

    def do_something( self ):
        tkinter.messagebox.showinfo( message = "Ok... I did something!" )

#------------------------------------------------------------------------------
# Script entry point...
#------------------------------------------------------------------------------

if __name__ == '__main__':

    root = Tk()
    root.title( 'Python - Tkinter Window with Menus' )
    root.withdraw() # Suppress unwanted window

    mainUI = myUserInterfaceClass( root,      # Set up the main GUI window
                                   '400x200', # Width & Height
                                   '+20+20',  # Initial X/Y screen location
                                   0        ) # Resizing turned off

    if not usingIDLE:   # Avoid IDLE or other Tkinter based IDEs
        root.mainloop() # Outer event loop
