import Entity
import Helper
import pygame
import ImageFiles


class Player(pygame.sprite.Sprite):
    currentLane = 0  # 0: Middle, -1: Left, 1: Right
    displaySurface = Helper.displaySurface
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = [Helper.RESOLUTION[0] * 0.5 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2 - playerSurf.get_height() * 0.5
                 + 600
                 ]  # (311.0, 202.8 for 750x1334 resolution)
    moveDistance = Helper.MOVE_DISTANCE

    @staticmethod
    def player_action(action, player):
        if 'move' in action:
            Player.player_move(action, player)
        elif 'idle' == action:
            pass
        elif 'open_inv' == action:
            pass

    @staticmethod
    def player_move(direction, player):  # needs four directions
        """
        Used for moving player upon swipe input, in future
        will be used for moving from room to room also.

        Args:
            direction -- string of the direction to move
            player -- this player class
        """
        if direction == 'move_right' and player.currentLane < 1:
            player_destination = player.playerPos[0] + player.moveDistance
            player.currentLane += 1

            while player.playerPos[0] < player_destination:
                player.playerPos[0] += Helper.MOVE_SPEED  # needs a loop in the "Main" script?
                Player.displaySurface.blit(ImageFiles.images['Background'], (0, 0))
                Player.displaySurface.blit(player.playerSurf, (player.playerPos[0], player.playerPos[1]))
                pygame.display.flip()

        elif direction == 'move_left' and player.currentLane > -1:
            player_destination = player.playerPos[0] - player.moveDistance
            player.currentLane -= 1

            while player.playerPos[0] > player_destination:
                player.playerPos[0] -= Helper.MOVE_SPEED  # needs a loop in the "Main" script?
                Player.displaySurface.blit(ImageFiles.images['Background'], (0, 0))
                Player.displaySurface.blit(player.playerSurf, (player.playerPos[0], player.playerPos[1]))

                pygame.display.flip()

