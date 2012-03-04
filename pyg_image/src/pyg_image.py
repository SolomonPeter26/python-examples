#------------------------------------------------------------------------------
#           Name: pyg_image.py
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python/Pygame script demonstrates how to load and 
#                 display an image file.
#------------------------------------------------------------------------------

import pygame

def main():
    
    pygame.init()	

    screen = pygame.display.set_mode( (640,480) )

    background = pygame.Surface( screen.get_size() )

    background.fill( (0,0,0) )

    image = pygame.image.load( "../images/pygame_powered.bmp" )

    image_position = image.get_rect()

    image_position.bottom = 240
    image_position.left = 200

    screen.blit( background, (0,0) )
    screen.blit( image, image_position )

    pygame.display.flip()

    while 1:
        
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()

        if keyinput[pygame.K_ESCAPE] or pygame.event.peek( pygame.QUIT ):
            break

        screen.blit( background, (0,0) )
        screen.blit( image, image_position )

        pygame.display.flip()

if __name__ == '__main__': main()
