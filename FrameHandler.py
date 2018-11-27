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
import random
from Room import Room
from pygame.locals import *

game_is_saved = False
room_is_populated = False
room_needs_advancing = False

pygame.time.set_timer(Helper.UPDATETIME, Helper.t)


def save_game(player):
    save_data = player
    print('Saving game...')
    pickle.dump(save_data, open("savegame.p", "wb"))
    return True


def populate_current_room():
    print('Populating current room...')
    if Room.current_room.is_populated is False:
        enemy_count = random.randint(1, 3)
    else:
        return False
    for i in range(0, enemy_count):
        Entity.enemy_list.append(Entity.Enemy(Room.current_room))
    print(str(Entity.enemy_list))
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


def clean_room():
    """
    ===========================================================================
    Removes projectiles and items in the room.
    ===========================================================================
    """
    Projectile.attackSprites.clear()


def event_handler(game_state, player):
    """
    ===========================================================================
    Handles keyboard/mouse inputs. Called every frame.

    :param game_state: current state as a string (ie. Main_Menu, Settings, etc)
    :param player: current instance of player class (should only be one)
    :return: input action (ie, moving left or right), new game_state
    ===========================================================================
    """

    now = datetime.datetime.now()
    global game_is_saved
    global room_is_populated
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
            elif event.key == K_m:
                print_data()
        elif event.type == MOUSEBUTTONDOWN:
            player_action = Inputs.read_mouse_movements(event.pos)

    if not room_is_populated:
        room_is_populated = populate_current_room()
    # if Entity.Enemy.numberOfOnscreenEnemies < 3:
    #     Entity.enemy_list.append(Entity.Enemy())
    # elif event.key == K_h and Entity.Enemy.numberOfOnscreenEnemies > 0:
    #     for enemy in Entity.enemy_list:
    #         enemy.__del__() todo: remove
    if not Player.Player.is_moving and not Player.Player.isLeavingRoom:
        if len(Entity.enemy_list) == 0:
            Player.Player.isLeavingRoom = True
            Room.advance_room()
            clean_room()

    if Room.current_room.position[1] >= Room.current_room_x\
            and Player.Player.isLeavingRoom:
        Player.Player.isLeavingRoom = False
        game_is_saved = False
        room_is_populated = False

    return player_action, game_state


def update(player, player_action):
    """
    ===========================================================================
    Calls update functions for player, enemies, and projectiles.
        Called every frame.

    :param player: current instance of player class
    :param player_action: input action, as defined in event_handler()
    ===========================================================================
    """

    if 'idle' in player_action and player.is_moving:
        player_action = player.move_direction

    player.player_action(player, player_action)

    if not player.inventoryIsOpen:
        for enemy in Entity.enemy_list:
            enemy.enemy_attack()

        for projectile in Projectile.attackSprites:
            projectile.update()


def renderer():  # to be called every frame to render every image in a list
    """
    ===========================================================================
    Blits everything to the screen that needs to be. Called every frame.
    ===========================================================================
    """

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
        Helper.DISPLAY_SURFACE.blit(projectile.sprite,
                                    (projectile.pos_x, projectile.pos_y)
                                    )

    for enemy in Entity.enemy_list:
        Helper.DISPLAY_SURFACE.blit(enemy.sprite, enemy.pos)

    pygame.time.Clock().tick(Helper.REFRESH_RATE)
    pygame.display.flip()

