import pygame
import Inputs
import Helper
import Entity
import Player
import ImageFiles
import Projectile
import datetime
import TimeOfDay
import pickle
import Item
import random
from Room import Room
from pygame.locals import *

game_is_saved = False
room_is_populated = False
room_needs_advancing = False

display_messages = []
display_delay = Helper.TEXT_DISPLAY_DELAY
display_time = Helper.TEXT_DISPLAY_TIME
display_position = list(Helper.TEXT_DISPLAY_POSITION)
time_since_last_display = pygame.time.get_ticks()
message_to_display = ''
current_player_level = 1
new_player_level = 1

pygame.time.set_timer(Helper.UPDATETIME, Helper.t)

pygame.font.init()

FONT_DISPLAY = pygame.font.Font(Helper.FONTS['Display'],
                                Helper.DEFAULT_FONT_SIZE)
FONT_DISPLAY_SMALL = pygame.font.Font(Helper.FONTS['Sans'],
                                      int(Helper.DEFAULT_FONT_SIZE - 6))


def save_game(player):
    """
    ===========================================================================
    Simple save game function.

    :param player: main instance of player class
    :return: true if the games has been saved
    ===========================================================================
    """
    save_data = player
    display_messages.append('Saving game...')
    pickle.dump(save_data, open("savegame.p", "wb"))
    return True


def populate_current_room():
    """
    ===========================================================================
    Adds a random number of enemies to the current room.

    :return: true if room has been filled, false if it already was
    ===========================================================================
    """

    if Room.current_room.is_populated is False:
        enemy_count = random.randint(1, 3)
    else:
        return False
    for i in range(0, enemy_count):
        Entity.enemy_list.append(Entity.Enemy(Room.current_room))
    return True


def clean_room():
    """
    ===========================================================================
    Removes projectiles and items in the room.
    ===========================================================================
    """
    Projectile.attackSprites.clear()
    for enemy in Entity.enemy_list:
        enemy.__del__()


def new_game():
    """
    ===========================================================================
    Resets the state of the game.
    ===========================================================================
    """
    Entity.health_bars.clear()
    Entity.enemy_list.clear()
    Projectile.attackSprites.clear()
    Player.Player.is_dead = False
    Player.Player.playerInstances = 0
    Player.Player.playerInstance = Player.Player()
    Player.Player.currentLane = 0
    global current_player_level
    current_player_level = 1

    Room.rooms_list.clear()

    Room.reset_room()

    first_room = Room()
    second_room = Room()

    Room.current_room = first_room
    Room.next_room = second_room

    Helper.LANES['left'][1] = False
    Helper.LANES['middle'][1] = False
    Helper.LANES['right'][1] = False

    populate_current_room()


def event_handler(game_state, player):
    """
    ===========================================================================
    Handles keyboard/mouse inputs. Called every frame.

    :param game_state: current state as a string (ie. Main_Menu, Settings, etc)
    :param player: current instance of player class (should only be one)
    :return: input action (ie, moving left or right), new game_state
    ===========================================================================
    """

    now = datetime.datetime.now()
    global game_is_saved
    global room_is_populated
    player_action = 'idle'

    if Entity.Enemy.numberOfOnscreenEnemies == 0 and not game_is_saved:
        game_is_saved = save_game(player)

    for event in pygame.event.get():
        if event.type == Helper.UPDATETIME:
            message = TimeOfDay.TimeOfDay.update_time_of_day(now)
            if message is not None and len(message) > 0:
                display_messages.append(message)
        if event.type == QUIT:
            game_state = 'Quit'
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_state = 'Main_Menu'
        elif event.type == MOUSEBUTTONDOWN:
            player_action = Inputs.read_mouse_down(event.pos)
        elif event.type == MOUSEBUTTONUP:
            player_action = Inputs.read_mouse_up(event.pos)

    if not room_is_populated:
        room_is_populated = populate_current_room()
    if not Player.Player.is_moving and not Player.Player.isLeavingRoom:
        if len(Entity.enemy_list) == 0:
            Player.Player.isLeavingRoom = True
            Room.advance_room()
            clean_room()

            # random roll for item

            if random.random() > 0.75:
                display_messages.append('Received a weapon!')
                Player.Player.Inventory.add_item(
                                            Item.Weapon(add_to_backpack=True)
                                                )
                Player.Player.Backpack.add_item(Player.Player.Inventory)

    if Room.current_room.position[1] >= Room.current_room_x\
            and Player.Player.isLeavingRoom:
        Player.Player.isLeavingRoom = False
        game_is_saved = False
        room_is_populated = False

    return player_action, game_state


def update(player, player_action):
    """
    ===========================================================================
    Calls update functions for player, enemies, and projectiles.
        Called every frame.

    :param player: current instance of player class
    :param player_action: input action, as defined in event_handler()
    ===========================================================================
    """

    global current_player_level

    if player.level != current_player_level:
        current_player_level = player.level
        display_messages.append('Leveled up!')

    for bar in Entity.health_bars:
        bar.health_bar_update()

    if 'idle' in player_action and player.is_moving:
        player_action = player.move_direction

    player.player_action(player, player_action)

    if not player.inventoryIsOpen:
        for enemy in Entity.enemy_list:
            enemy.enemy_attack()

        for projectile in Projectile.attackSprites:
            projectile.update()


def renderer():
    """
    ===========================================================================
    Blits everything to the screen that needs to be.
        Called every frame to render every image in a list.
    ===========================================================================
    """

    if Room.prev_room:
        Helper.DISPLAY_SURFACE.blit(Room.prev_room.texture,
                                    Room.prev_room.position
                                    )
    Helper.DISPLAY_SURFACE.blit(Room.current_room.texture,
                                Room.current_room.position
                                )
    Helper.DISPLAY_SURFACE.blit(Room.next_room.texture,
                                Room.next_room.position
                                )

    Room.move_room()

    Helper.DISPLAY_SURFACE.blit(Player.Player.playerSurf,
                                Player.Player.playerPos
                                )

    # display health bars

    for bar in Entity.health_bars:
        bar_background = pygame.Surface((bar.size[0] + 4, bar.size[1] + 4))
        bar_background.fill((0, 0, 0))
        bar_surface = pygame.Surface((bar.size[0] *
                                      (bar.health / bar.max_health),
                                      bar.size[1]
                                      ))

        bar_surface.fill(bar.colour)
        Helper.DISPLAY_SURFACE.blit(bar_background, (bar.pos[0] - 2,
                                                     bar.pos[1] - 2))
        Helper.DISPLAY_SURFACE.blit(bar_surface, (bar.pos[0], bar.pos[1]))

    for projectile in Projectile.attackSprites:
        Helper.DISPLAY_SURFACE.blit(projectile.sprite,
                                    (projectile.pos_x, projectile.pos_y)
                                    )

    # display inventory if it is open

    if Player.Player.inventoryIsOpen:
        Helper.DISPLAY_SURFACE.blit(
            ImageFiles.images['UI']['Inventory_Background'],
            Helper.INVENTORY_POSITION
        )

    # display enemies

    for enemy in Entity.enemy_list:
        Helper.DISPLAY_SURFACE.blit(enemy.sprite, enemy.pos)

    global message_to_display
    global time_since_last_display

    if message_to_display == '':

        if time_since_last_display < pygame.time.get_ticks() + display_delay\
                and len(display_messages) > 0:

            message_to_display = display_messages.pop(0)
            time_since_last_display = pygame.time.get_ticks()
    else:
        if time_since_last_display + display_time < pygame.time.get_ticks():
            message_to_display = ''

    text_surface = FONT_DISPLAY.render(message_to_display,
                                       False,
                                       Helper.WHITE)

    if text_surface.get_width() > Helper.DISPLAY_SURFACE.get_width():
        messages = message_to_display.split(',')
        index = 0
        for message in messages:
            if message is not '':
                if message not in display_messages:
                    display_messages.insert(0 + index, message)
                    index += 1

        text_surface = FONT_DISPLAY.render('',
                                           False,
                                           Helper.WHITE)
    # create strings for stats
    stats = [
        str('Level : ' + str(Player.Player.playerInstance.level)),
        str('HP : '
            + str(Player.Player.playerInstance.health)
            + '/'
            + str(Player.Player.playerInstance.max_health)),
        str('XP : '
            + str(Player.Player.playerInstance.exp)
            + '/'
            + str(Player.Player.playerInstance.exp_to_level_up))
    ]

    # offset text if inventory is not open

    vertical_offset = 500 if not Player.Player.inventoryIsOpen else 0

    for stat_key in Player.Player.playerInstance.stats.keys():
        stats.append(
            stat_key + ' : '
            + str(Player.Player.playerInstance.stats[stat_key]['Value'])
        )

    for stat_index in range(0, len(stats)):
        stat_surface = FONT_DISPLAY_SMALL.render(stats[stat_index],
                                                 False,
                                                 Helper.BLACK)
        Helper.DISPLAY_SURFACE.blit(stat_surface,
                                    (Helper.INVENTORY_POSITION[0] + 40,
                                     Helper.INVENTORY_POSITION[1] + 20
                                     * stat_index + 100 + vertical_offset)
                                    )
        stat_index += 1

    stats.clear()

    # display inventory

    for slot in range(0, Player.Player.Backpack.size):
        item_surf = None if slot > len(Player.Player.Backpack.items) - 1\
            else Player.Player.Backpack.items[slot].\
            weapon_thumbnail.convert_alpha() \
            if type(Player.Player.Backpack.items[slot]) == Item.Weapon \
            else None

        if item_surf is None:
            item_surf = pygame.Surface((80, 80))
            item_surf.fill(Helper.WHITE)

        row = 0 if slot < int(Player.Player.Backpack.size / 2) else 1
        column = slot if slot < int(Player.Player.Backpack.size / 2)\
            else slot - Player.Player.Backpack.size / 2

        position = [
            Helper.INVENTORY_POSITION[0] + 350 +
            (item_surf.get_width() + 20) * column,
            Helper.INVENTORY_POSITION[1] + 100 +
            (item_surf.get_height() + 20) * row + vertical_offset
                    ]

        Helper.DISPLAY_SURFACE.blit(item_surf, position)

        del item_surf

    Helper.DISPLAY_SURFACE.blit(text_surface,
                                (10, 10))

    pygame.time.Clock().tick(Helper.REFRESH_RATE)
    pygame.display.flip()
