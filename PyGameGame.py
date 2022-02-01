import pygame

# Color Defs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# Color Defs

# Params
display_width = 800
display_height = 600
gameCaption = 'Deja Vu Ive Seen This Game Before'
# Params

pygame.init()   # Init pygame

gameDisplay = pygame.display.set_mode((display_width, display_height)) # Set Display size
pygame.display.set_caption(gameCaption) # Set Display Caption
clock = pygame.time.Clock()  # Set Clock for the game

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()