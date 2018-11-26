# this should only have one function in, this function can be moved elsewhere
import pygame
import Inputs
import Helper
import Entity
import Player
import ImageFiles
import Projectile
import datetime
import TimeOfDay
import pickle
from Room import Room
from pygame.locals import *

game_is_saved = False

pygame.time.set_timer(Helper.UPDATETIME, Helper.t)


def save_game(player):
    save_data = player
    # print('Saving game...')
    pickle.dump(save_data, open("savegame.p", "wb"))
    return True


def print_data():
    if Room.next_room:
        print('Next room position is', str(Room.next_room.position))
    if Room.current_room:
        print('Current room position is', str(Room.current_room.position))
    if Room.prev_room:
        print('Previous room position is', str(Room.prev_room.position))
    print('Room positions are', str(Room.next_room_x),
          str(Room.current_room_x),
          str(Room.prev_room_x))
    print('Movement step is', str(Room.room_move_speed))


def event_handler(game_state, player):
    now = datetime.datetime.now()
    global game_is_saved
    player_action = 'idle'
    if Entity.Enemy.numberOfOnscreenEnemies == 0 and game_is_saved is False:
        game_is_saved = save_game(player)
    for event in pygame.event.get():
        if event.type == Helper.UPDATETIME:
            TimeOfDay.TimeOfDay.update_time_of_day(now)
        if event.type == QUIT:
            game_state = 'Quit'
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state = 'Main_Menu'
            elif event.key == K_g and Entity.Enemy.numberOfOnscreenEnemies < 3:
                Entity.enemy_list.append(Entity.Enemy())
            elif event.key == K_h and Entity.Enemy.numberOfOnscreenEnemies > 0:
                for enemy in Entity.enemy_list:
                    enemy.__del__()
            elif event.key == K_w and not Player.Player.is_moving:
                if len(Entity.enemy_list) == 0:
                    Player.Player.isLeavingRoom = True
            elif event.key == K_n:
                Room.advance_room()
                game_is_saved = False
            elif event.key == K_m:
                print_data()

        elif event.type == MOUSEBUTTONDOWN:
            player_action = Inputs.read_mouse_movements(event.pos, player)
    return player_action, game_state


def update(player, player_action):
    if 'idle' in player_action and player.is_moving:
        player_action = player.move_direction

    player.player_action(player, player_action)

    if not player.inventoryIsOpen:
        for enemy in Entity.enemy_list:
            enemy.enemy_update()

        for projectile in Projectile.attackSprites:
            projectile.update()
        # print(str(player.playerRect.contains(projectile.rect)))


def renderer():  # to be called every frame to render every image in a list

    if Room.prev_room:
        Helper.DISPLAY_SURFACE.blit(Room.prev_room.texture, Room.prev_room.position)
    Helper.DISPLAY_SURFACE.blit(Room.current_room.texture, Room.current_room.position)
    Helper.DISPLAY_SURFACE.blit(Room.next_room.texture, Room.next_room.position)

    Room.move_room()

    Helper.DISPLAY_SURFACE.blit(Player.Player.playerSurf, Player.Player.playerPos)

    if Player.Player.inventoryIsOpen:
        Helper.DISPLAY_SURFACE.blit(
            ImageFiles.images['UI']['Inventory_Background'],
            Helper.INVENTORY_POSITION
        )

    for projectile in Projectile.attackSprites:
        Helper.DISPLAY_SURFACE.blit(projectile.sprite, (projectile.pos_x, projectile.pos_y))

    for enemy in Entity.enemy_list:
        Helper.DISPLAY_SURFACE.blit(enemy.sprite, enemy.pos)

    pygame.time.Clock().tick(Helper.REFRESH_RATE)
    pygame.display.flip()

