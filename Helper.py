import pygame


# Main display variables
REFRESH_RATE = 60
RESOLUTION = (750, 1334)
DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION)


# Dictionary for fonts
FONTS = dict(
    Display='./Resources/Visual/Fonts/inverted.ttf',
    Sans='./Resources/Visual/Fonts/rounded-pixelfont.ttf'
            )


# Lane positions and whether or not they are occupied
LANES = dict(
    left=[(150, 250), False],
    middle=[(375, 250), False],
    right=[(600, 250), False]
)


# VARIABLES FOR MENU

# Fonts for the menu
pygame.font.init()
MENU_SANS = pygame.font.Font(FONTS['Display'], 30)
SMALL_SANS = pygame.font.Font(FONTS['Display'], 20)

# Colours for the menu screen
BLACK = (0, 0, 0)
BRONZE = (124, 91, 51)
GOLD = (147, 117, 53)
HIGHLIGHT = (150, 120, 100, 20)
DARK_GRAY = (69, 69, 69)

# Surfaces for the menu buttons
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

TEXTSURF_DESPACITO = SMALL_SANS.render('Hello World', False, HIGHLIGHT)


# CHARACTER VARIABLES

# distance moved for input to be registered as a swipe
SWIPE_DISTANCE = 90

# time for player to be allowed to hold down a swipe
MAX_SWIPE_TIME = 80

# distance the onscreen character moves
MOVE_DISTANCE = LANES['middle'][0][0] - LANES['left'][0][0]

# base speed value for player projectiles
PROJECTILE_SPEED = 20

# default player attack cooldown in milliseconds
PLAYER_ATTACK_COOLDOWN = 750

# distance for character move steps
MOVE_SPEED = 10


# default exp required for level up
EXP_REQUIRED = 100

# Player stats
STATS = dict(
    CON=dict(
        Name='Constitution',
        Value=10
    ),
    END=dict(
        Name='Endurance',
        Value=10
    ),
    STR=dict(
        Name='Strength',
        Value=10
    ),
    DEX=dict(
        Name='Dexterity',
        Value=10
    ),
    AGL=dict(
        Name='Agility',
        Value=10
    ),
    LCK=dict(
        Name='Luck',
        Value=10
    ),
    FTH=dict(
        Name='Faith',
        Value=10
    )
)


# DISPLAY VARIABLES

# Health bar colours
GREEN = (0, 155, 0)
YELLOW = (155, 155, 0)
RED = (155, 10, 0)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

# health bar dimensions
HEALTH_BAR_SIZE = (137, 8)
HEALTH_BAR_THRESHOLDS = [.3, .6, .9]
HEALTH_BAR_COLOURS = [RED, YELLOW, GREEN, WHITE]

# onscreen position of inventory
INVENTORY_POSITION = (15, 970)

# onscreen position for in-game text display
TEXT_DISPLAY_POSITION = (RESOLUTION[0] / 2, 250)

# delay for displaying in-game messages
TEXT_DISPLAY_DELAY = 2000

# for how long the text is displayed
TEXT_DISPLAY_TIME = 1500

# default font size
DEFAULT_FONT_SIZE = 24


# ENEMY AND ROOM VARIABLES

# Tuples containing elements for naming items, rooms_list, entities etc
Affinities = ('Chaos', 'Abyss', 'Void', 'Eldritch')
ELEMENTS = ('Water', 'Air', 'Earth', 'Fire')
MODIFIERS_ELEMENTAL_T1 = ('Dew', 'Whistles', 'Pebbles', 'Ashes')
MODIFIERS_ELEMENTAL_T2 = ('Splashes', 'Breezes', 'Rocks', 'Smoulders')
MODIFIERS_ELEMENTAL_T3 = ('Waves', 'Typhoons', 'Boulders', 'Flames')
MODIFIERS_BONUS = ('Cursed', 'Blessed')
QUALITY = ('Broken', 'Chipped', 'Mundane', 'Tempered', 'Pristine')
WEAPONS = ('Nodachi', 'Katana', 'Tekkan', 'Hachiwari')
UPGRADES = ('+0', '+1', '+2', '+3', '+4', '+5')

# Event used for time-of-day specific features (called every second)
UPDATETIME, t = pygame.USEREVENT+1, 1000

TIME_OF_DAY = dict(
    morning=([400, 1000],
             (80, 15, 15),
             ', the monsters return to normal'
             ),
    noon=([1000, 1600],
          (135, 80, 0),
          ', the monsters are now weakened'
          ),
    evening=([1600, 2200],
             (80, 15, 15),
             ', the monsters return to normal'
             ),
    night=([2200, 400],
           (25, 50, 75),
           ', the monsters are stronger'
           ),
    night_blood_moon=([2200, 400],
                      (80, 40, 50),
                      ', the monsters are enraged!'
                      ),
    night_new_moon=([2200, 400],
                    (38, 118, 168),
                    ', the monsters are enraged!'
                    )
)

room_tutorial_path = './Resources/Visual/Textures/Rooms/room.png'

# Defining colors for the 4 elements

Modifiers_Elemental_Colours = ((28, 58, 89),
                               (244, 213, 141),
                               (28, 89, 29),
                               (206, 78, 55))

# Usage: Select element from tuples and parse it to generator

# Order: QUALITY + WEAPON_NAME + 'OF' +  Modifiers_Elemental
# + Upgrade + (Modifier_Bonus)
# Example: Chipped Nodachi of Smoulders +2 (Cursed)


room_encounter_type = (
                       'ascension',
                       'a shrine',
                       'a fork in the road',
                       'a villager in need',
                       'rubble on the road'
                       )

# Custom events
