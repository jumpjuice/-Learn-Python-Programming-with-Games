'''
Created on Aug 24, 2018
@author: Burkhard A. Meier
'''







# imports
import pygame
from pygame.locals import *         # imports lots of constants (e.g. K_UP, K_SPACE)

# initialization
pygame.init()                       # don't forget to make this initialization call

game_surface = pygame.display.set_mode((600, 400))   # create the game surface, passing in a size (width, height)

# game logic


# game loop
run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == QUIT:          # from pygame.locals import *, no need to prepend pygame.QUIT
            run_game = False

# exit game
pygame.quit()






























