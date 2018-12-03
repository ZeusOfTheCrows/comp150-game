import pygame
import sys
import FrameHandler
import Helper
import Menu
import Player
import MapGenerator
from Room import Room

pygame.init()

# variables
REFRESH_RATE = Helper.REFRESH_RATE
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE
FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
DISPLAY_SURFACE.fill((79, 51, 44))
player = Player.Player()
MapGenerator.run_separator()


game_state = 'Main_Menu'
prev_game_state = ''
is_paused = False
running = True
game_is_saved = False

first_room = Room()
second_room = Room()


while running:

    while game_state == 'Main_Menu':
        game_state, loaded_data = Menu.menu_update()

    while game_state == 'Settings':
        game_state = Menu.settings_menu_update()

    while game_state == 'New_Game':
        # event handling section
        if loaded_data:
            aux_player = loaded_data
            print(aux_player.health)
        player_action, game_state = FrameHandler.event_handler(game_state,
                                                               player
                                                               )

        # action handling section
        FrameHandler.update(player, player_action)

        # display handling section
        FrameHandler.renderer()

    if game_state == 'Death_Screen':
        game_state = Menu.game_over_screen_update()

    if game_state == 'Quit':
        running = False

    # cap fps
    FPS_CLOCK.tick(REFRESH_RATE)

MapGenerator.run_remover()  # cleans generated tiles from Resources/Tiles

pygame.quit()
sys.exit()
