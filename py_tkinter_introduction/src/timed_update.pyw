import tkinter
import time

curtime = ''
label = tkinter.Label()
label.pack( padx = 50, pady = 50 )

def update():
    global curtime
    newtime = time.strftime( '%H:%M:%S' )
    if newtime != curtime:
        curtime = newtime
        label.config( text = curtime )
    label.after( 200, update )

update()
label.mainloop()
