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
from pygame.locals import *

pygame.time.set_timer(Helper.UPDATETIME, Helper.t)


def save_game(player):
    save_data = player
    print('Saving game...')
    pickle.dump(save_data, open("savegame.p", "wb"))


def event_handler(game_state, player):
    now = datetime.datetime.now()
    player_action = 'idle'
    if Entity.Enemy.numberOfOnscreenEnemies == 0:
        save_game(player)
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

    Helper.DISPLAY_SURFACE.blit(ImageFiles.images['Background'], (0, 0))
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

