import pygame, LoadImages
from pygame.locals import *

pygame.init()

# variables
size = (750, 334)
black = (0, 0, 0)

# guff
controlsSurface = pygame.display.set_mode(size)
controlsSurface.fill(black)


def read_mouse_movements(mouse_x, mouse_y):
    reading_mouse_change = True
    while reading_mouse_change:
        if MOUSEBUTTONUP:
            reading_mouse_change = False

        if pygame.event.get()



    pass
