import pygame
import ImageFiles
import os
import Helper

"""Map Generation, including tile separation"""

pygame.init()


screen = pygame.display.set_mode(Helper.RESOLUTION, 0, 32)
pygame.display.set_caption('Map Generation')

tilemap = ImageFiles.images['Tilemap'].convert_alpha()

tile_path = './Resources/Visual/Tiles/'

if not os.path.exists(tile_path):
    os.makedirs(tile_path)

# Number of tiles on the x and y axis
tilemap_size_x = 9
tilemap_size_y = 9

# Index keeps track of each tile
tile_index = 0


# Function for removing empty tiles from directory
def empty_tile_removal(path):

    for filename in os.listdir(path):
        if filename.endswith('.png'):
            image = pygame.image.load(path + filename)
            is_empty = True
            for x in range(0, image.get_width()):
                for y in range(0, image.get_height()):
                    if image.get_at((x, y)).a != 0:
                        is_empty = False
                        break
            if is_empty:
                os.remove(path + filename)


# Separator for tiles
def separate_tiles(size_x, size_y, tilemap, path, index):
    for x in range(0, size_x):
        for y in range(0, size_y):

            tile_area = pygame.Rect(y * 25, x * 25, 24, 24)
            tile = tilemap.subsurface(tile_area)
            pygame.image.save(tile, path + 'tile' + str(index) + '.png')
            index += 1

    print('Finished splitting')

    empty_tile_removal(path)

    print('Finished removing empty tiles')


# Removes tiles at end of game
def all_tile_removal(path):

    for filename in os.listdir(path):
        if filename.endswith('.png'):
            os.remove(path + filename)


finished = False


def run_separator():
    separate_tiles(tilemap_size_x, tilemap_size_y, tilemap, tile_path, tile_index)


def run_remover():
    all_tile_removal(tile_path)
