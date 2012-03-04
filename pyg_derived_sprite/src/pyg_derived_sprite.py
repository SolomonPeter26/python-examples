#------------------------------------------------------------------------------
#           Name: pyg_derived_sprite.py
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python/Pygame script demonstrates how to create a  
#                 custom sprite class for a 2D game by deriving a new class
#                 from PyGame's built-in Sprite class.
#------------------------------------------------------------------------------

import pygame

#------------------------------------------------------------------------------
# Name: loadImageFile()
# Desc: 
#------------------------------------------------------------------------------

def loadImageFile( fileName, useColorKey = False ):
    
    try:
        image = pygame.image.load( fileName )
    except pygame.error:
        raise IOError from "File " + fileName + " not found."

    # To speed things up, convert the images to SDL's internal format.
    image = image.convert()

    if useColorKey is True:
        # Use the color of the pixel located at (0,0) as our color-key
        colorkey = image.get_at( (0,0) )
        image.set_colorkey( colorkey, pygame.RLEACCEL )

    # Return the image
    return image
    
#------------------------------------------------------------------------------
# Name: MySprite
# Desc: 
#------------------------------------------------------------------------------

class MySprite( pygame.sprite.Sprite ):

    def __init__( self ):
        
        # Intialize Sprite, our base class
        pygame.sprite.Sprite.__init__( self )

        self.image = loadImageFile( "../images/mario.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 150)

        surface = pygame.display.get_surface()
        self.area = surface.get_rect()

        self.x_velocity = 5.0
        self.y_velocity = 1.0

    def update( self ):

        # Simulate gravity by constantly adding some amount to the
        # sprite's Y velocity. This will pull the sprite down
        self.y_velocity += 0.5

        # Now, move the sprite...
        self.rect.move_ip( (self.x_velocity, self.y_velocity ) )

        if self.rect.left < self.area.left or self.rect.right > self.area.right:
            # If the sprite is about to leave the screen's area, invert its 
            # X velocity so it will change its direction of travel
            self.x_velocity = -(self.x_velocity)
            self.rect.move_ip( (self.x_velocity, self.y_velocity ) )

            # Since we just bounced off the screen's left or right side,
            # flip the image so it seems to be going the other way.
            self.image = pygame.transform.flip( self.image, True, False )

        if self.rect.bottom > self.area.bottom:
            # If the sprite hits the bottom of the screen's area, invert its  
            # Y velocity so it will bounce back up
            self.y_velocity = -(self.y_velocity)
            self.rect.move_ip( (self.x_velocity, self.y_velocity ) )

#------------------------------------------------------------------------------
# Name: main()
# Desc: 
#------------------------------------------------------------------------------

def main():

    # Initialize pygame and create a window or screen to render to
    pygame.init()
    screen = pygame.display.set_mode( (640, 480) )

    # Create a background for our screen
    background = pygame.Surface( screen.get_size() )
    background = background.convert()
    background.fill( (255, 255, 255) )

    # Initialize our sprite object
    sprite = MySprite()
    allsprites = pygame.sprite.RenderPlain( sprite )

    # Initialize a clock for animating the sprite's motion
    clock = pygame.time.Clock()

    # Ok... we're done initializing! Time to enter the script's
    # main loop and start drawing our sprite.

    while 1:
        clock.tick( 60 )

        # Handle input events
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        if keyinput[pygame.K_ESCAPE] or pygame.event.peek(pygame.QUIT):
            break

        # Update our sprite object
        allsprites.update()

        # Display the background
        screen.blit( background, (0, 0) )
        allsprites.draw( screen )

        # Display the sprite
        pygame.display.flip()

# This calls the 'main' function when this script is executed
if __name__ == '__main__': main()
