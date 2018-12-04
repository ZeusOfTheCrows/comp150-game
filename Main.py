import pygame
import sys
import Helper
import Menu
import Player
import MapGenerator
import FrameHandler
from Room import Room

pygame.init()

# variables
REFRESH_RATE = Helper.REFRESH_RATE
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE
FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption('Sekai Saviour')
DISPLAY_SURFACE.fill((79, 51, 44))

player_has_died = False

player = Player.Player()
MapGenerator.run_separator()


game_state = 'Main_Menu'
prev_game_state = ''
is_paused = False
running = True
game_is_saved = False
loaded_data = None

# generate first 2 rooms

first_room = Room()
second_room = Room()

# load music

pygame.mixer.init()
pygame.mixer_music.load('./Resources/Audio/Sounds/main_theme.wav')
pygame.mixer_music.play(-1)

while running:

    while game_state == 'Main_Menu':
        game_state, loaded_data = Menu.menu_update()

    while game_state == 'Settings':
        game_state = Menu.settings_menu_update()

    while game_state == 'New_Game':
        # event handling section

        if Player.Player.is_dead:

            Player.Player.is_dead = False

            is_paused = False
            game_is_saved = False

            FrameHandler.new_game()

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

        if Player.Player.is_dead:
            prev_game_state = "New_Game"
            game_state = "Death_Screen"
            break

    if game_state == 'Death_Screen':
        game_state = Menu.game_over_screen_update()

    if game_state == 'Quit':
        running = False

    # cap fps
    FPS_CLOCK.tick(REFRESH_RATE)

MapGenerator.run_remover()  # cleans generated tiles from Resources/Tiles

pygame.quit()
sys.exit()
