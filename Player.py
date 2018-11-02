import Entity
import Helper
import pygame
import ImageFiles


class Player(Entity.Entity):

    is_moving = False
    move_direction = ''

    currentLane = 0  # 0: Middle, -1: Left, 1: Right
    displaySurface = Helper.DISPLAY_SURFACE
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = [Helper.RESOLUTION[0] * 0.5 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2 - playerSurf.get_height() * 0.5
                 + 600
                 ]  # (311.0, 202.8 for 750x1334 resolution)
    moveDistance = Helper.MOVE_DISTANCE
    inventoryPosition = Helper.INVENTORY_POSITION
    inventoryIsOpen = False

    player_destination = 0

    def __init__(self):
        Entity.Entity.__init__(self)
        self.health = Entity.Entity.defaultHealth

    @staticmethod
    def player_action(action, player):
        if 'move' in action:
            Player.player_move(action, player)
        elif 'idle' == action:
            pass

    @staticmethod
    def inventory_update(action):
        if 'switch_inv' == action:
            Player.inventoryIsOpen = not Player.inventoryIsOpen
        elif 'open_inv' == action:
            Player.inventoryIsOpen = True
        elif 'close_inv' == action:
            Player.inventoryIsOpen = False

    @staticmethod
    def player_move(direction, player):  # needs four directions
        """
        Used for moving player upon swipe input, in future
        will be used for moving from room to room also.

        Args:
            direction -- string of the direction to move
            player -- this player class
        """
        if not player.is_moving:


            if direction == 'move_right' and player.currentLane < 1:
                player.currentLane += 1
                player.move_direction = direction
                player.player_destination = player.playerPos[0] + player.moveDistance
            elif player.currentLane > -1:
                player.currentLane -= 1
                player.move_direction = direction
                player.player_destination = player.playerPos[0] - player.moveDistance

            player.is_moving = True

        if player.is_moving and player.move_direction == 'move_right':
            if player.playerPos[0] < player.player_destination and player.inventoryIsOpen == False:
                player.playerPos[0] += Helper.MOVE_SPEED
            else:
                player.direction = ''
                player.move_direction = ''