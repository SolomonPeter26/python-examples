#------------------------------------------------------------------------------
#           Name: pyg_fonts.py
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python/Pygame script demonstrates how to create and
#                 render on-screen text using fonts.
#------------------------------------------------------------------------------

import pygame

def main():
    
    pygame.display.init()
    pygame.font.init()

    fontDefault = pygame.font.Font( None, 48 )
    fontTimes   = pygame.font.Font( "../fonts/times.ttf", 24 )
    fontCourier = pygame.font.Font( "../fonts/cour.ttf", 24 )

    screen = pygame.display.set_mode( (640,480) )

    while 1:
        
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        
        if keyinput[pygame.K_ESCAPE] or pygame.event.peek( pygame.QUIT ):
            break

        screen.fill( (0,0,0) )

        string = fontDefault.render( "This line uses the default font!", 0, (255,0,0))
        screen.blit( string, (100,100) )

        string = fontTimes.render( "This line uses the Times New Roman font!", 0, (0,255,0))
        screen.blit( string, (100,200) )

        string = fontCourier.render( "This line uses the Courier New font!", 0, (0,0,255))
        screen.blit( string, (100,300) )

        pygame.display.flip()

if __name__ == '__main__': main()
