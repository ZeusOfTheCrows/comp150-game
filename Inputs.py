import Player
import Helper
import pygame
from pygame.locals import *

pygame.init()
# inputTimer = pygame.time.Clock()


# variables
swipeDistance = Helper.SWIPE_DISTANCE
maxSwipeTime = Helper.MAX_SWIPE_TIME
# readingMouseChange = False


def read_mouse_movements(mouse_position):
    """
    ===========================================================================
    Reads swipe inputs, input with the mouse on PC.

    :param mouse_position: position of mouse button down.
    :return: input command as a string (ie. move_right).
    ===========================================================================
    """

    mouse_down_x, mouse_down_y = mouse_position
    input_command = 'none'
    elapsed_time = pygame.time.get_ticks()  # used for timer

    global readingMouseChange
    readingMouseChange = True
    while readingMouseChange:  # while loop to read mouse/swipe movements

        for event in pygame.event.get():

            # if the mouse button has been release, or the specified time has elapsed
            if event.type == MOUSEBUTTONUP or (pygame.time.get_ticks() -
                                               elapsed_time) >= maxSwipeTime:

                # sets the mouse position manually, as otherwise there would be no event position
                if (pygame.time.get_ticks() - elapsed_time) >= maxSwipeTime:
                    event.pos = pygame.mouse.get_pos()
                    # todo:comment this @zeus

                mouse_up_x, mouse_up_y = event.pos
                input_distance_h = mouse_up_x - mouse_down_x
                input_distance_v = mouse_up_y - mouse_down_y

                # global readingMouseChange
                readingMouseChange = False

                if input_distance_h >= swipeDistance:
                    input_command = 'move_right'
                elif input_distance_h <= -swipeDistance:
                    input_command = 'move_left'
                elif input_distance_v >= swipeDistance:
                    input_command = 'close_inv'
                elif input_distance_v <= -swipeDistance:
                    input_command = 'open_inv'
                elif abs(input_distance_h) < swipeDistance\
                        and\
                        abs(input_distance_v) < swipeDistance:
                    input_command = 'attack'

                # player.player_action(input_command)
                return input_command

# todo: remove this monolithic mess ^ @zeus


mouseDownX, mouseDownY = 0, 0
readingMouseChange = False


def read_mouse_down(mouse_position):
    """
    ===========================================================================
    First half of the input function. Sets the mouse down position (to be used
        in the next half), and sets "reading mouse change" to true.
        This and read_mouse_up() read swipe inputs, input with the mouse on PC.

    :param mouse_position: position of mouse button down.
    :return: input command as a string (should always be 'none' at this stage).
    ===========================================================================
    """

    global mouseDownX, mouseDownY
    mouseDownX, mouseDownY = mouse_position
    input_command = 'none'
    global readingMouseChange
    readingMouseChange = True

    return input_command


def read_mouse_up(mouse_position):
    """
    ===========================================================================
    Second half of the input function. Calculates swipe inputs, input with the
        mouse on PC., based on the mouse coordinates from read_mouse_down(),
                                    and sets "reading mouse change" to false.


    :param mouse_position: position of mouse button up.
    :return: input command as a string (ie. 'move_right').
    ===========================================================================
    """

    mouse_up_x, mouse_up_y = mouse_position
    input_distance_h = mouse_up_x - mouseDownX
    input_distance_v = mouse_up_y - mouseDownY

    global readingMouseChange
    readingMouseChange = False

    if input_distance_h >= swipeDistance:
        input_command = 'move_right'
    elif input_distance_h <= -swipeDistance:
        input_command = 'move_left'
    elif input_distance_v >= swipeDistance:
        input_command = 'close_inv'
    elif input_distance_v <= -swipeDistance:
        input_command = 'open_inv'
    elif abs(input_distance_h) < swipeDistance \
            and \
            abs(input_distance_v) < swipeDistance:
        input_command = 'attack'
    else:  # this should never happen, it's only in here as a failsafe.
        input_command = 'none'

    # player.player_action(input_command)
    return input_command
