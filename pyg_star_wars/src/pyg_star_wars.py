#------------------------------------------------------------------------------
#           Name: pyg_star_wars.py
#         Author: Kevin Harris
#  Last Modified: 05/05/10
#    Description: This Python/Pygame script demonstrates how to create a simple
#                 Space Invaders clone.
#------------------------------------------------------------------------------

import random
import os
import pygame

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

#------------------------------------------------------------------------------
# Name: loadImageFile()
# Desc: 
#------------------------------------------------------------------------------

def loadImageFile( name, useColorKey = False ):

    fullname = os.path.join( "../data", name )

    try:
        image = pygame.image.load( fullname )
    except pygame.error:
        raise IOError from "Image File " + fullname + " not found."

    # To speed things up, convert the images to SDL's internal format.
    image = image.convert()

    if useColorKey is True:
        # Use the color of the pixel located at (0,0) as our colorkey
        colorkey = image.get_at( (0,0) )
        image.set_colorkey( colorkey, pygame.RLEACCEL )

    # Return the image
    return image

#------------------------------------------------------------------------------
# Name: loadSoundFile()
# Desc: 
#------------------------------------------------------------------------------

def loadSoundFile( name ):

    class NoneSound:
        def play( self ): pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join( "../data", name )

    try:
        sound = pygame.mixer.Sound( fullname )
    except pygame.error:
        raise IOError from "Sound File " + fullname + " not found."

    return sound

#------------------------------------------------------------------------------
# Name: XWing
# Desc: 
#------------------------------------------------------------------------------

class XWing( pygame.sprite.Sprite ):

    def __init__( self ):
        # Intialize Sprite, which is our base class
        pygame.sprite.Sprite.__init__( self )
        self.image = loadImageFile( "xwing.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT)
        self.x_velocity = 0
        self.y_velocity = 0

    def update( self ):
        self.rect.move_ip( (self.x_velocity, self.y_velocity) )

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= SCREEN_HEIGHT/2:
            self.rect.top = SCREEN_HEIGHT/2
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#------------------------------------------------------------------------------
# Name: TIEFighter
# Desc: 
#------------------------------------------------------------------------------
 
class TIEFighter( pygame.sprite.Sprite ):

    def __init__( self, startx ):
        # Intialize Sprite, which is our base class
        pygame.sprite.Sprite.__init__( self )
        self.image = loadImageFile( "tie_fighter.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.centerx = startx
        self.rect.centery = 120
        self.x_velocity = random.randint( -5, 5 )
        self.y_velocity = random.randint( -5, 5 )
        
    def update( self ):
        self.rect.move_ip( (self.x_velocity, self.y_velocity) )

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.x_velocity = -(self.x_velocity)

        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT/2:
            self.y_velocity = -(self.y_velocity)

        # Randomize firing
        fire = random.randint( 1, 60 )
        if fire == 1:
            tiefighterLaserSprites.add( TIEFighterLaser( self.rect.midbottom ) )
            tiefighterShotFX.play()

#------------------------------------------------------------------------------
# Name: XWingLaser
# Desc: 
#------------------------------------------------------------------------------

class XWingLaser( pygame.sprite.Sprite ):
    
    def __init__( self, startpos ):
        # Intialize Sprite, which is our base class
        pygame.sprite.Sprite.__init__( self )
        self.image = loadImageFile( "rebel_laser.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.center = startpos

    def update( self ):
        if self.rect.bottom <= 0:
            self.kill()
        else:
            self.rect.move_ip( (0,-4) )
            
#------------------------------------------------------------------------------
# Name: TIEFighterLaser
# Desc: 
#------------------------------------------------------------------------------

class TIEFighterLaser( pygame.sprite.Sprite ):
    
    def __init__( self, startpos ):
        # Intialize Sprite, which is our base class
        pygame.sprite.Sprite.__init__( self )
        self.image = loadImageFile( "empire_laser.bmp", True )
        self.rect = self.image.get_rect()
        self.rect.midtop = startpos
        
    def update( self ):
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
        else:
            self.rect.move_ip( (0,4) )

#------------------------------------------------------------------------------
# Name: main()
# Desc: 
#------------------------------------------------------------------------------

def main():

    random.seed()
    pygame.init()
    #screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN )
    #screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF )
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption( "Star Wars" )

    # Create the background
    background_image = loadImageFile( "background.bmp" )
    screen.blit(background_image, (0,0))
    #pygame.mouse.set_visible( False )

    # Load sound FXs
    explode1FX = loadSoundFile( "explode1.wav" )
    #explode2FX = loadSoundFile( "explode2.wav" )
    global tiefighterShotFX
    tiefighterShotFX = loadSoundFile( "empire_laser.wav" )
    xwingShotFX = loadSoundFile( "rebel_laser.wav" )

    # Initialize the player's X-Wing
    xwingSprite = pygame.sprite.RenderClear()
    xwing = XWing()
    xwingSprite.add( xwing )
    xwingLaserSprites = pygame.sprite.RenderClear()

    # Initialize the TIE Fighters (start the game with 3 fighters)
    tiefighterSprites = pygame.sprite.RenderClear()
    tiefighterSprites.add( TIEFighter( 150 ) )
    tiefighterSprites.add( TIEFighter( 400 ) )
    tiefighterSprites.add( TIEFighter( 650 ) )
    global tiefighterLaserSprites
    tiefighterLaserSprites = pygame.sprite.RenderClear()

    # Initialize some control variables
    running = True
    addTieFighterCounter = 0
    clock = pygame.time.Clock()

    while running is True:
        clock.tick( 60 )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    xwing.x_velocity = -4
                elif event.key == pygame.K_RIGHT:
                    xwing.x_velocity = 4
                elif event.key == pygame.K_UP:
                    xwing.y_velocity = -4
                elif event.key == pygame.K_DOWN:
                    xwing.y_velocity = 4
                elif event.key == pygame.K_SPACE:
                    xwingLaserSprites.add( XWingLaser( xwing.rect.midtop ) )
                    xwingShotFX.play()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    xwing.x_velocity = 0
                elif event.key == pygame.K_RIGHT:
                    xwing.x_velocity = 0
                elif event.key == pygame.K_UP:
                    xwing.y_velocity = 0
                elif event.key == pygame.K_DOWN:
                    xwing.y_velocity = 0

        # Add another TIE Fighter
        addTieFighterCounter += 1
        if addTieFighterCounter >= 200:
            tiefighterSprites.add( TIEFighter( 320 ) )
            addTieFighterCounter = 0

        # Update all sprites
        xwingSprite.update()
        xwingLaserSprites.update()
        tiefighterSprites.update()
        tiefighterLaserSprites.update()

        # See if any of the player's laser shots hit any of the TIE Fighters
        for hit in pygame.sprite.groupcollide( tiefighterSprites, xwingLaserSprites, 1, 1 ):
            explode1FX.play()

        # Clear everything that was drawn to the screen last time
        tiefighterLaserSprites.clear( screen, background_image )
        tiefighterSprites.clear( screen, background_image )
        xwingLaserSprites.clear( screen, background_image)
        xwingSprite.clear( screen, background_image )

        # Draw everything
        tiefighterLaserSprites.draw( screen )
        xwingLaserSprites.draw( screen )
        tiefighterSprites.draw( screen )
        xwingSprite.draw( screen )

        pygame.display.flip()

#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
