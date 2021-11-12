import pygame, sys, random
from pygame import key
from pygame import sprite
from pygame.display import get_active
from pygame.locals import *
from pygame.sprite import Group, collide_rect, spritecollideany
#from land_two import main2
from random import randint

pygame.init()

# Game setup
WHITE_COLOR = (255, 255, 255)
FPS = 150
fpsClock = pygame.time.Clock()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
title = ("Mars Rover Driving Game!")
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN = pygame.display.set_caption(title)

def main():
    looping = True
    # Import rover image
    ROVER = pygame.image.load('Assets/rover.png').convert_alpha()
    ROVER = pygame.transform.scale(ROVER, (35, 30))
    roverX = 20
    roverY = 40

    # Import Hazard1 Gif
    HAZARD1 = pygame.image.load('Assets/turnado.gif').convert_alpha()
    HAZARD1 = pygame.transform.scale(HAZARD1, (35, 30))
    hazard1X = 180
    hazard1Y = 0

    # Import Hazard2 Gif
    HAZARD2 = pygame.image.load('Assets/turnado.gif').convert_alpha()
    HAZARD2 = pygame.transform.scale(HAZARD2, (35, 30))
    hazard2X = 500
    hazard2Y = 480
    
    # Main game looping
    while looping:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Screen background
        game_screen.fill(WHITE_COLOR)
        new_game = pygame.image.load("Assets/terrain.jpg").convert_alpha()
        tileX = 0
        tileY = 0
        cropX = 0
        cropY = 0
        cropWidth = SCREEN_WIDTH
        cropHeight = SCREEN_HEIGHT
        game_screen.blit(new_game, (tileX, tileY), (cropX, cropY, cropWidth, cropHeight))
        pygame.display.update()
        fpsClock.tick(FPS)
        
        # Process rover control settings
        roverLeft = pygame.transform.flip(ROVER, False, True)
        roverDown = pygame.transform.flip(ROVER, False, True)
        roverMoving = ROVER
        pressed = pygame.key.get_pressed()
        game_screen.blit(roverMoving, (roverX, roverY))

        # Process hazard1 control settings
        hazardDown = pygame.transform.flip(HAZARD1, False, True)
        hazardMoving = HAZARD1
        game_screen.blit(hazardMoving, (hazard1X, hazard1Y))

        # Process hazard2 control settings
        hazard2Down = pygame.transform.flip(HAZARD2, False, True)
        hazard2Forward = pygame.transform.flip(HAZARD2, True, False)
        hazard2Moving = HAZARD2
        game_screen.blit(hazard2Moving, (hazard2X, hazard2Y))
        pygame.display.update()

        # Gate data current position to control hazard x,y
        info = pygame.display.Info()
        sw = info.current_w
        sh = info.current_h

        # Control the hazard1
        hazard1Y += 2
        if hazard1Y < 0 or hazard1Y > sw-120:
            hazard1Y = 2
            hazard1X = random.randint(0, 400)

        # Control the hazard2
        hazard2Y -= 2
        if hazard2Y < 0 or hazard2Y > sw-120:
            hazard2Y = 480
            hazard2X = random.randint(0, 300)

        # control the rover with key arrows direction
        if (pressed[K_RIGHT] or pressed[K_d]) :
            roverX = roverX + 3
            roverMoving = ROVER
        elif (pressed[K_LEFT] or pressed[K_a]) :
            roverX = roverX - 3
            roverMoving = roverLeft
        elif (pressed[K_UP] or pressed[K_w]) :
            roverY = roverY - 3
            roverMoving = ROVER
        elif (pressed[K_DOWN] or pressed[K_s]) :
            roverY = roverY + 3
            roverMoving = roverDown

        # If the rover touch the border of the screen, he change of level
        # elif roverX < 0 or roverX > sw-0:
        #     main2()
        
        # Close the game if the key q is pressed
        elif pressed[K_q] :
            event.type == pygame.QUIT
            looping = False
#-----------------------------------------------------------------------------------------#       
#-------- Control the hazard, if the rover touch the hazard, game over or lossing point---#
#------------------------------ Need to work in this part --------------------------------#
#-----------------------------------------------------------------------------------------#
        if (roverX and roverY) == (hazard1X and hazard1Y) or (roverX and roverY) == (hazard2X and hazard2Y):
            print("Game Over")
        
          
if __name__ == "__main__":
    main()
