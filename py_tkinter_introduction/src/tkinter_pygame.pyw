#------------------------------------------------------------------------------
#           Name: tkinter_pygame.py
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: 
#------------------------------------------------------------------------------

import os
import sys
import tkinter
import tkinter.messagebox
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLACK = ( 0, 0, 0 )
ball_speed = [2, 2]

# Create the root window using tkinter.
root = tkinter.Tk()
root.title( "Pygame embeded into tkinter" )
root.geometry( "640x480" )

# Create a frame in the window to hold other widgets.
frame = tkinter.Frame( root )
frame.grid()
frame.pack( fill = tkinter.BOTH, expand = tkinter.YES )

#def delete_handler():
#    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
#        root.destroy()
#
#root.protocol( "WM_DELETE_WINDOW", delete_handlerb )

#
# Mouse events...
#

def button_handler( event ):
    print( "tkinter - button_handler" )

def b1_motion_handler( event ):
    print( "tkinter - b1_motion_handler" )

def button_release_1_handler( event ):
    print( "tkinter - button_release_1_handler" )

def mouse_wheel_handler( event ):
    print( "tkinter - mouse_wheel_handler" )

frame.bind_all( "<Button-1>", button_handler )
frame.bind_all( "<B1-Motion>", b1_motion_handler )
frame.bind_all( "<ButtonRelease-1>", button_release_1_handler )
frame.bind_all( "<MouseWheel>", mouse_wheel_handler )

#
# Keyboard events...
#

def key_handler( event ):
    print( "tkinter - " + str( event.char ) )

    if event.keysym == "Escape":
        print( "tkinter - Escape keysym = " + str( event.keysym ) )

frame.bind_all( "<Key>", key_handler )


# Create a label in the frame.
label = tkinter.Label( frame, text = "Hello from Tkinter!" )
label.grid()


# To embed pygame inside tkinter, we need to tell pygame's underlying SDL 
# window that the pygame window is going to be a child window of a tkinter 
# widget.
os.environ["SDL_WINDOWID"] = str( frame.winfo_id() )

# We also need to disable DirectX on Windows if we're going to embed pygame 
# inside tkinter. If we don't the pygame image will not remain aligned inside 
# tkinter.
if sys.platform.startswith( "win" ):
    os.environ["SDL_VIDEODRIVER"] = "windib"

pygame.init()
screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
background = pygame.Surface( screen.get_size() )
background.fill( BLACK )
image = pygame.image.load( "../images/ball.bmp" )

ball_rect = image.get_rect()

def update_pygame():

    global ball_rect

    for event in pygame.event.get():         
        if event.type == pygame.QUIT:
            print( "pygame - QUIT" )
            pygame.quit()
            sys.exit()

    keyinput = pygame.key.get_pressed()

    if keyinput[pygame.K_ESCAPE]:
        print( "pygame - K_ESCAPE" )
        pygame.quit()
        root.destroy()
        sys.exit()

    if keyinput[pygame.K_SPACE]:
        print( "pygame - K_SPACE" )

    ball_rect = ball_rect.move( ball_speed )

    if ball_rect.left < 0 or ball_rect.right > SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball_rect.top < 0 or ball_rect.bottom > SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]

    screen.fill( BLACK )
    screen.blit( image, ball_rect )
    pygame.display.flip()

    # We're done updating. Tell the tkinter widget to wait after a 
    # moment and then call us again for our next update.
    frame.after( 10, update_pygame )

# Start our timed update which will update pygame.
update_pygame()

# Start the window's event loop.
root.mainloop()





