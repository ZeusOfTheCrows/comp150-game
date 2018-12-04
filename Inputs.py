import Helper
import pygame

pygame.init()

# variables
swipeDistance = Helper.SWIPE_DISTANCE
maxSwipeTime = Helper.MAX_SWIPE_TIME
readingMouseChange = False
mouse_down_pos = []


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

    mouse_down_pos.clear()
    mouse_down_pos.extend(mouse_position)
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

    mouse_up_pos = mouse_position
    input_distance_h = mouse_up_pos[0] - mouse_down_pos[0]
    input_distance_v = mouse_up_pos[1] - mouse_down_pos[1]

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
    else:  # this should never happen, it's only in here as a fail safe.
        input_command = 'none'

    return input_command
