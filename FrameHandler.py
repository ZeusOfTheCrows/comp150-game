import pygame
import Inputs
import Helper
import Entity
import Player
import ImageFiles
import Projectile
import datetime
import TimeOfDay
from pygame.locals import *

pygame.time.set_timer(Helper.UPDATETIME, Helper.t)


def event_handler(game_state, player):  # todo: remove parameter?
    """
    ===========================================================================
    Handles keyboard/mouse inputs. Called every frame.

    :param game_state: current state as a string (ie. Main_Menu, Settings, etc)
    :param player: current instance of player class (should only be one)
    :return: input action (ie, moving left or right), new game_state
    ===========================================================================
    """

    now = datetime.datetime.now()
    player_action = 'idle'
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
                Entity.enemy_list.clear()
            elif event.key == K_w and not Player.Player.is_moving:
                if len(Entity.enemy_list) == 0:
                    Player.Player.isLeavingRoom = True
        elif event.type == MOUSEBUTTONDOWN:
            player_action = Inputs.read_mouse_movements(event.pos)
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
    Blits everything to the screen that needs to be. Called every frame.
    """

    Helper.DISPLAY_SURFACE.blit(ImageFiles.images['Background'], (0, 0))
    Helper.DISPLAY_SURFACE.blit(Player.Player.playerSurf,
                                Player.Player.playerPos
                                )

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

