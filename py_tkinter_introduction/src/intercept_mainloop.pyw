import tkinter
import tkinter.messagebox

class Tk( tkinter.Tk ):

    def __init__( self, *args, **kw ):
        tkinter.Tk.__init__( self, *args, **kw )

        def mainloop( w, n = 0 ):
            # Your code here...
            print( "Intercepting  mainloop!", w._w )
            self.tk.mainloop( n )

        tkinter.Misc.mainloop = mainloop

root = Tk()

button = tkinter.Button( root, text = 'Quit', command = root.quit )
button.pack( padx = 50, pady = 50 )
button.focus_set()

root.mainloop()

