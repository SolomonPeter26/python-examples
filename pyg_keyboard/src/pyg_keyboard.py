#------------------------------------------------------------------------------
#           Name: pyg_keyboard.py
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python/Pygame script demonstrates how to move an image 
#                 using keyboard input.
#------------------------------------------------------------------------------

import pygame

def main():
    
    pygame.init()

    screen = pygame.display.set_mode( (640,480) )
    
    background = pygame.Surface( screen.get_size() )

    background.fill( (255,255,255) )

    sprite = pygame.image.load( "../images/galaga_ship.bmp" )

    spriteRect = sprite.get_rect()

    spriteRect.centerx = (640 / 2)
    spriteRect.centery = (480 / 2)

    screen.blit( background, (0,0) )
    screen.blit( sprite, spriteRect )

    pygame.display.flip()

    while 1:
        
        pygame.event.pump()
        keyinput = pygame.key.get_pressed()
        
        if keyinput[pygame.K_ESCAPE] or pygame.event.peek(pygame.QUIT):
            break

        if keyinput[pygame.K_LEFT]:
            spriteRect.centerx -= 2
        
        if keyinput[pygame.K_RIGHT]:
            spriteRect.centerx += 2

        if keyinput[pygame.K_UP]:
            spriteRect.centery -= 2		

        if keyinput[pygame.K_DOWN]:
            spriteRect.centery += 2		

        screen.blit( background, (0,0) )
        screen.blit( sprite, spriteRect )

        pygame.display.flip()

if __name__ == '__main__': main()
