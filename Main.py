import pygame, sys, LoadImages
from pygame.locals import *

pygame.init()

# variables
refreshRate = 60
resolution = (750, 1000)
# colours
darkBrown = (79, 51, 44)
lightBrown = (107, 74, 55)
darkYellow = (124, 91, 51)
lightYellow = (147, 117, 53)
black = (0, 0, 0)
darkGrey = (63, 63, 63)
midGrey = (127, 127, 127)
lightGrey = (191, 191, 191)

# guff
displaySurface = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
displaySurface.fill(darkBrown)

# game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # redraw display
    pygame.display.flip()

    # cap fps
    clock.tick(refreshRate)