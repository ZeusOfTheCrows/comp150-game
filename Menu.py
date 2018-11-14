import pygame
import sys
import Helper
import MenuHelper
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


def draw_menu(save_file_exists):  # Draws rectangles to represent the 'buttons'
    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonNewGame'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_NEWGAME, (130, 484))

    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonSettings'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_SETTINGS, (130, 684))

    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonQuit'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_QUIT, (510, 684))

    if save_file_exists:
        pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['buttonContinue'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_CONTINUE, (480, 484))

    elif not save_file_exists:
        pygame.draw.rect(DISPLAY_SURFACE, DARK_GRAY, buttons['buttonContinue'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_BLACKCONTINUE, (480, 484))

    else:
        raise ValueError('\'save_file_exists\' is neither true nor false.'\
                         'This is not Schrodinger\'s save_file, fix it.')


def draw_settings_menu():
    pygame.draw.rect(DISPLAY_SURFACE, BRONZE, buttons['settingsBackground'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_DESPACITO, (625, 940))

    pygame.draw.rect(DISPLAY_SURFACE, GOLD, buttons['settingsExit'])
    DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_SETTINGSEXIT, (80, 910))


def check_buttons(click_pos, save_file_exists):
    """
    Checks which 'button' was clicked,
    can assign functions to each separate button
    Arguments:
        click_pos -- position of the mouse click
    """
    if buttons['buttonQuit'].collidepoint(click_pos):
        print("Button clicked: Quit")
        return 'Quit'

    elif buttons['buttonNewGame'].collidepoint(click_pos):
        print("Button clicked: New Game")
        return 'New_Game'

    elif buttons['buttonContinue'].collidepoint(click_pos):
        if save_file_exists:
            print("Button clicked: Continue")
            # return 'Continue'
        else:
            print("Button clicked: Continue. However, save file not found.")

    elif buttons['buttonSettings'].collidepoint(click_pos):
        print("Button clicked: Settings")
        return 'Settings'

    return 'Main_Menu'


def check_settings_buttons(click_pos):
    if buttons['settingsExit'].collidepoint(click_pos):
        print("Button clicked: Exit Settings")
        return 'Main_Menu'

    return 'Settings'


def highlight_buttons(mx, my, save_file_exists):  # Draws a highlight over a button on mouse-over

    if buttons['buttonNewGame'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonNewGame'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHNEWGAME, (130, 484))

    elif buttons['buttonContinue'].collidepoint(mx, my):
        if save_file_exists:
            pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonContinue'])
            DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHCONTINUE, (480, 484))

    elif buttons['buttonSettings'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonSettings'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHSETTINGS, (130, 684))

    elif buttons['buttonQuit'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['buttonQuit'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHQUIT, (510, 684))


def highlight_settings_buttons(mx, my):  # Draws a highlight over a button on mouse-over
    if buttons['settingsExit'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT, buttons['settingsExit'])
        DISPLAY_SURFACE.blit(MenuHelper.TEXTSURF_HIGHSETTINGSEXIT, (80, 910))


def menu_update():
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
