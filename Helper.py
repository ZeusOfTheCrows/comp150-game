import pygame

# todo: docstrings in
'''
Audio
AudioFiles
Helper
ImageFiles
Item
MapGenerator
Menu
MenuHelper
Player
Projectile
Room
TimeOfDay
'''

REFRESH_RATE = 60
RESOLUTION = (750, 1334)
DISPLAY_SURFACE = pygame.display.set_mode(RESOLUTION)

# Lane positions and whether or not they are occupied
LANES = dict(
    left=[(150, 250), False],
    middle=[(375, 250), False],
    right=[(600, 250), False]
)

# distance moved for input to be registered as a swipe
SWIPE_DISTANCE = 90

# distance the onscreen character moves
MOVE_DISTANCE = LANES['middle'][0][0] - LANES['left'][0][0]

# base speed value for player projectiles
PROJECTILE_SPEED = 20

# default player attack cooldown in milliseconds
PLAYER_ATTACK_COOLDOWN = 750

# distance for character move steps
MOVE_SPEED = 10

# onscreen position of inventory
INVENTORY_POSITION = (15, 970)

# Tuples containing elements for naming items, rooms, entities etc
Affinities = ('Chaos', 'Abyss', 'Void', 'Eldritch')
ELEMENTS = ('Water', 'Air', 'Earth', 'Fire')
MODIFIERS_ELEMENTAL_T1 = ('Dew', 'Whistles', 'Pebbles', 'Ashes')
MODIFIERS_ELEMENTAL_T2 = ('Splashes', 'Breezes', 'Rocks', 'Smoulders')
MODIFIERS_ELEMENTAL_T3 = ('Waves', 'Typhoons', 'Boulders', 'Flames')
MODIFIERS_BONUS = ('Cursed', 'Blessed')
QUALITY = ('Broken', 'Chipped', 'Mundane', 'Tempered', 'Pristine')
WEAPONS = ('Nodachi', 'Katana', 'Tekkan', 'Hachiwari')
UPGRADES = ('+0', '+1', '+2', '+3', '+4', '+5')

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

# Room variables:

room_encounter_type = (
                       'ascension',
                       'a shrine',
                       'a fork in the road',
                       'a villager in need',
                       'rubble on the road'
                       )

# Custom events

UPDATETIME, t = pygame.USEREVENT+1, 1000


