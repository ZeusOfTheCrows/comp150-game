import pygame
import sys
import time  # only currently necessary for testing purposes
import ImageFiles
import Helper
import Menu
import Inputs
import Player
import MapGenerator
from pygame.locals import *

pygame.init()


# variables
refreshRate = 60

DISPLAY_SURFACE = Helper.DISPLAY_SURFACE
FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
DISPLAY_SURFACE.fill(Helper.darkBrown)
player = Player.Player()
MapGenerator.run_separator()

# game loop
running = True

game_state = 'Main_Menu'

is_paused = False

inv_is_open = False
while running:

    while game_state == 'Main_Menu':
        game_state = Menu.menu_update()
        DISPLAY_SURFACE.blit(ImageFiles.images['Player'], (0, 0))

    while game_state == 'New_Game' and running and not is_paused:
        # game loop event handling section
        if not is_paused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_state = 'Main_Menu'
                        break
                    elif event.key == K_a:
                        player.player_action('move_left', player)
                    elif event.key == K_d:
                        player.player_action('move_right', player)
                    elif event.key == K_i:
                        # DISPLAY_SURFACE.blit(ImageFiles.images['UI']['Inventory_Background'], (0, 0))
                        inv_is_open = player.inventory_update('switch_inv', inv_is_open)
                        print('toggling inventory')
                elif event.type == MOUSEBUTTONDOWN and not inv_is_open:  # start to read swipe input
                    action = Inputs.read_mouse_movements(event.pos, player)
                    player.player_action(action, player, inv_is_open)
                    inv_is_open = player.inventory_update(action)
                elif event.type == MOUSEBUTTONDOWN and inv_is_open:
                    action = Inputs.read_mouse_movements(event.pos, player)
                    inv_is_open = player.inventory_update(action, inv_is_open)
                else:
                    player.player_action('idle', player)

            # game loop action section

            # game loop display section

            DISPLAY_SURFACE.blit(ImageFiles.images['Background'], (0, 0))
            DISPLAY_SURFACE.blit(player.playerSurf, player.playerPos)

            if inv_is_open:
                DISPLAY_SURFACE.blit(ImageFiles.images['UI']['Inventory_Background'], (0, 0))

            pygame.display.flip()
        else:
            print('GAME IS PAUSED')
            pygame.time.delay(300)

    if game_state == 'Quit':
        running = False

    # cap fps
    FPS_CLOCK.tick(refreshRate)

MapGenerator.run_remover()

pygame.quit()
sys.exit()
