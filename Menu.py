import pygame
import sys
import Helper
import MenuHelper
import pickle
from pygame.locals import *

pygame.init()
pygame.font.init()

BLACK = MenuHelper.BLACK
BRONZE = MenuHelper.BRONZE
GOLD = MenuHelper.GOLD
HIGHLIGHT = MenuHelper.HIGHLIGHT
DARK_GRAY = MenuHelper.DARK_GRAY

FPS = 60
FPS_CLOCK = pygame.time.Clock()
DISPLAY_SURFACE = Helper.DISPLAY_SURFACE
pygame.display.set_caption('Sekai Saviour')

buttons = dict(
    buttonNewGame=pygame.Rect(50, 434, 300, 150),
    buttonContinue=pygame.Rect(400, 434, 300, 150),
    buttonSettings=pygame.Rect(50, 634, 300, 150),
    buttonQuit=pygame.Rect(400, 634, 300, 150),
    settingsBackground=pygame.Rect(25, 375, 700, 600),
    settingsExit=pygame.Rect(50, 900, 100, 50)
    )


def draw_menu(continue_button_clickable):
    """
    ===========================================================================
    Draws rectangles to represent the buttons
    :param continue_button_clickable: greys out continue button if there
                                                is no existing save file
    ===========================================================================
    """

    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonNewGame'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_NEWGAME, (130, 484))

    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonSettings'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_SETTINGS, (130, 684))

    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonQuit'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_QUIT, (510, 684))

    if continue_button_clickable:
        pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonContinue'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_CONTINUE, (480, 484))

    elif not continue_button_clickable:
        pygame.draw.rect(DISPLAY_SURFACE, DARK_GRAY, buttons['buttonContinue'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_BLACKCONTINUE, (480, 484))

    else:  # todo: remove debug code? @joycourier
        raise ValueError('\'save_file_exists\' is neither true nor false.'
                         'This is not Schrodinger\'s save_file, fix it.')


def draw_settings_menu():
    """
    ===========================================================================
    Draws rectangles to represent the setting menu background and back button.
    ===========================================================================
    """

    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['settingsBackground'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_DESPACITO, (625, 940))

    pygame.draw.rect(DISPLAY_SURFACE, GOLD, buttons['settingsExit'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_SETTINGSEXIT, (80, 910))


def check_buttons(click_pos, save_file_exists):
    """
    ===========================================================================
    Checks which 'button' was clicked, can assign
        functions to each separate button.
    :param click_pos: position of the mouse click
    :param save_file_exists: whether a previous save file exists
    :return: the game state (as a string)
    ===========================================================================
    """
    if buttons['buttonQuit'].collidepoint(click_pos):
        print("Button clicked: Quit")
        return 'Quit', None

    elif buttons['buttonNewGame'].collidepoint(click_pos):
        print("Button clicked: New Game")
        return 'New_Game', None

    elif buttons['buttonContinue'].collidepoint(click_pos):
        if save_file_exists:
            print("Button clicked: Continue")
            # return 'Continue'
        else:
            print("Button clicked: Continue. However, save file not found.")
    elif buttons['buttonSettings'].collidepoint(click_pos):
        print("Button clicked: Settings")
        return 'Settings', None

    return 'Main_Menu', None


def check_settings_buttons(click_pos):
    """
    todo: docstring
    :param click_pos:
    :return:
    """

    if buttons['settingsExit'].collidepoint(click_pos):
        print("Button clicked: Exit Settings")
        return 'Main_Menu'

    return 'Settings'


def highlight_buttons(mouse_x, mouse_y, make_continue_clickable):
    """
    ===========================================================================
    Draws a highlight over a button on mouse-over.

    :param mouse_x: current mouse horizontal position (not click)
    :param mouse_y: current mouse vertical position (not click)
    :param make_continue_clickable: makes continue button unclickable
                                            if save file des not exist
    ===========================================================================
    """

    if buttons['buttonNewGame'].collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonNewGame'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHNEWGAME, (130, 484))

    elif buttons['buttonContinue'].collidepoint(mouse_x, mouse_y):
        if make_continue_clickable:
            pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonContinue'])
            DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHCONTINUE, (480, 484))

    elif buttons['buttonSettings'].collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonSettings'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHSETTINGS, (130, 684))

    elif buttons['buttonQuit'].collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonQuit'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHQUIT, (510, 684))


def highlight_settings_buttons(mouse_x, mouse_y):
    """
    ===========================================================================
    Draws a highlight over a button on mouse-over.
    :param mouse_x: current mouse horizontal position (not click)
    :param mouse_y: current mouse vertical position (not click)
    ===========================================================================
    """

    if buttons['settingsExit'].collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['settingsExit'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHSETTINGSEXIT, (80, 910))


def menu_update():
    """
    ===========================================================================
    todo: fill this in.
        Also, why is there a while loop outside of the main loop @joycourier?
    ===========================================================================
    """

    (mouse_x, mouse_y) = (0, 0)
    save_file_exists = False
    while True:
        DISPLAY_SURFACE.fill(BLACK)
        draw_menu(save_file_exists)
        for event in pygame.event.get():
            # stores most recent mouse movement in two variables
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print('Key pressed: Escape - Closing game...')
                    pygame.quit()
                    sys.exit()

            # check if a button was clicked on mouse click
            elif event.type == MOUSEBUTTONUP:
                click_pos = pygame.mouse.get_pos()
                return check_buttons(click_pos, save_file_exists)

        highlight_buttons(mouse_x, mouse_y, save_file_exists)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def settings_menu_update():
    """
    ===========================================================================
    todo: fill this in.
        Also, why is there a while loop outside of the main loop @joycourier?
    ===========================================================================
    """

    (mouse_x, mouse_y) = (0, 0)
    while True:
        DISPLAY_SURFACE.fill(BLACK)
        draw_settings_menu()

        for event in pygame.event.get():
            # stores most recent mouse movement in two variables
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print('Key pressed: Escape - Exiting menu...')
                    return 'Main_Menu'

            # check if a button was clicked on mouse click
            elif event.type == MOUSEBUTTONUP:
                click_pos = pygame.mouse.get_pos()
                return check_settings_buttons(click_pos)

        highlight_settings_buttons(mouse_x, mouse_y)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
