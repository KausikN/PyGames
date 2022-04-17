"""
PyGame Test Game
"""

# Imports
import pygame

# Main Vars
# Color Defs
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
}

# Main Functions
def main(display_width, display_height, displayObj=print):
    gameCaption = "Deja Vu Ive Seen This Game Before"

    # Init pygame
    pygame.init()
    # Set Display size
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    # Set Display Caption
    pygame.display.set_caption(gameCaption)
    # Set Clock for the game
    clock = pygame.time.Clock()
    # Start Game
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            displayObj(event)
        pygame.display.update()
        clock.tick(60)

# # Driver Code
# # Params
# display_width = 800
# display_height = 600
# # Params