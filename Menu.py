import pygame
from pygame.locals import *

# research blit, it is better than draw

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURFACE = pygame.display.set_mode((750, 1000), 0, 32)
pygame.display.set_caption('S E K A I SAVIOR')

buttons = dict(
    buttonNewGame=pygame.Rect(50, 600, 300, 150),
    buttonContinue=pygame.Rect(400, 600, 300, 150),
    buttonSettings=pygame.Rect(50, 800, 300, 150),
    buttonQuit=pygame.Rect(400, 800, 300, 150),
    menuSettingsExit=pygame.Rect(25, 375, 700, 600),
    menuExit=pygame.Rect(50, 900, 100, 50)
    )

BLACK = (0, 0, 0)  # currently used for the background
BACKGROUNDGOLD = (124, 91, 51)  # currently unused
BUTTONGOLD = (147, 117, 53)  # colour of the buttons
HIGHLIGHT = (150, 120, 100, 20)  # colour of the highlight, not sure how to get alpha working but we won't bother


def draw_menu():  # Draws rectangles to represent the 'buttons'
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttons['buttonNewGame'])
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttons['buttonContinue'])
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttons['buttonSettings'])
    pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttons['buttonQuit'])


def check_buttons():  # Checks which 'button' was clicked, can assign functions to each separate button
    if buttons['buttonNewGame'].collidepoint(clickPos):
        print("Button clicked: New Game")
    elif buttons['buttonContinue'].collidepoint(clickPos):
        print("Button clicked: Continue")
    elif buttons['buttonSettings'].collidepoint(clickPos):
        print("Button clicked: Settings")
        # settings_menu()
    elif buttons['buttonQuit'].collidepoint(clickPos):
        print("Button clicked: Quit")
        pygame.quit()


# def settings_menu():
    # pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttons['menuSettings'])
    # pygame.draw.rect(DISPLAYSURFACE, BUTTONGOLD, buttons['menuSettingsExit'])


def highlight_buttons(mx, my):  # Draws a highlight over a button when moused over
    if buttons['buttonNewGame'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT,buttons['buttonNewGame'])
    elif buttons['buttonContinue'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttons['buttonContinue'])
    elif buttons['buttonSettings'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttons['buttonSettings'])
    elif buttons['buttonQuit'].collidepoint(mx, my):
        pygame.draw.rect(DISPLAYSURFACE, HIGHLIGHT, buttons['buttonQuit'])


while True:
    DISPLAYSURFACE.fill(BLACK)
    draw_menu()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos  # stores most recent mouse movement in two variables
        elif event.type == MOUSEBUTTONUP:
            clickPos = pygame.mouse.get_pos()
            check_buttons()  # when the mouse button is clicked, we check if a button was clicked

    highlight_buttons(mousex, mousey)
    pygame.display.update()
    fpsClock.tick(FPS)
