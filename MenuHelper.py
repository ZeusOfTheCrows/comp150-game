import pygame

MENU_SANS = pygame.font.SysFont('Comic Sans MS', 30)
SMALL_SANS = pygame.font.SysFont('Comic Sans MS', 20)

BLACK = (0, 0, 0)
BRONZE = (124, 91, 51)
GOLD = (147, 117, 53)
HIGHLIGHT = (150, 120, 100, 20)
DARK_GRAY = (69, 69, 69)

TEXTSURF_NEWGAME = MENU_SANS.render('New Game', False, GOLD)
TEXTSURF_HIGHNEWGAME = MENU_SANS.render('New Game', False, BRONZE)

TEXTSURF_CONTINUE = MENU_SANS.render('Continue', False, GOLD)
TEXTSURF_HIGHCONTINUE = MENU_SANS.render('Continue', False, BRONZE)
TEXTSURF_BLACKCONTINUE = MENU_SANS.render('Continue', False, BLACK)

TEXTSURF_SETTINGS = MENU_SANS.render('Settings', False, GOLD)
TEXTSURF_HIGHSETTINGS = MENU_SANS.render('Settings', False, BRONZE)

TEXTSURF_QUIT = MENU_SANS.render('Quit', False, GOLD)
TEXTSURF_HIGHQUIT = MENU_SANS.render('Quit', False, BRONZE)

TEXTSURF_SETTINGSEXIT = SMALL_SANS.render('Back', False, BRONZE)
TEXTSURF_HIGHSETTINGSEXIT = SMALL_SANS.render('Back', False, BLACK)

TEXTSURF_DESPACITO = SMALL_SANS.render('Despacito', False, HIGHLIGHT)
