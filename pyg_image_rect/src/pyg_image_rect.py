#------------------------------------------------------------------------------
#           Name: pyg_image_rect.py
#         Author: Kevin Harris
#  Last Modified: 02/23/11
#    Description: This Python/Pygame script demonstrates how to move or place
#                 a simple image by accessing its Rect (rectangle) data.
#------------------------------------------------------------------------------

import sys
import pygame

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
BLACK = (0, 0, 0)
ballSpeed = [2,2]

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )

ballImage = pygame.image.load( "../images/ball.bmp" )

ballRect = ballImage.get_rect()

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballRect = ballRect.move( ballSpeed )

    if ballRect.left < 0 or ballRect.right > SCREEN_WIDTH:
        ballSpeed[0] = -ballSpeed[0]

    if ballRect.top < 0 or ballRect.bottom > SCREEN_HEIGHT:
        ballSpeed[1] = -ballSpeed[1]

    screen.fill( BLACK )
    screen.blit( ballImage, ballRect )
    pygame.display.flip()
