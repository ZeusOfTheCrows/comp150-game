import Entity
import Helper
import ImageFiles
import Inventory
import Projectile
import pygame
import random


class Player(Entity.Entity):
    """
    Player class. Used for instantiating the Player.
    Most functions are static, given that there can only be a single instance
    of the Player. Attempting to create multiple instances will result in
    an error.
    """

    is_moving = False
    move_direction = ''
    isLeavingRoom = False

    # initialize most variables

    currentLane = 0  # 0: Middle, -1: Left, 1: Right
    displaySurface = Helper.DISPLAY_SURFACE
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = [Helper.RESOLUTION[0] * 0.5
                 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2
                 - playerSurf.get_height() * 0.5
                 + 600
                 ]
    playerRect.x = 0
    playerRect.y = 0
    moveDistance = Helper.MOVE_DISTANCE
    inventoryPosition = Helper.INVENTORY_POSITION
    projectileSpeed = Helper.PROJECTILE_SPEED
    attackCooldown = Helper.PLAYER_ATTACK_COOLDOWN
    lastAttack = 0
    playerInstances = 0
    playerInstance = None
    baseDamage = 50
    moveSpeed = Helper.MOVE_SPEED
    health = 1
    max_health = 1
    is_dead = False
    inventoryIsOpen = False
    hasWeaponEquipped = False
    weaponEquipped = None
    Inventory = None
    Backpack = None
    healthBar = None
    player_destination = 0

    def __init__(self):

        Player.playerPos = [Helper.RESOLUTION[0] * 0.5
                            - Player.playerSurf.get_width() * 0.5,
                            Helper.RESOLUTION[1] * 0.2
                            - Player.playerSurf.get_height() * 0.5
                            + 600
                            ]
        Player.playerRect.x = Player.playerPos[0]
        Player.playerRect.y = Player.playerPos[1]
        Player.moveSpeed = Helper.MOVE_SPEED
        Player.moveDistance = Helper.MOVE_DISTANCE
        if Player.playerInstances == 0:
            Player.playerInstances += 1
        else:
            raise ValueError('Attempted to create another instance of Player')
        Entity.Entity.__init__(self)

        self.exp_to_level_up = Helper.EXP_REQUIRED
        self.exp = 0

        Player.max_health = Entity.Entity.defaultHealth * 100

        Player.health = Player.max_health

        Player.healthBar = Entity.HealthBar(self)

        Player.playerInstance = self

        Player.Inventory = Inventory.Inventory()

        Player.Backpack = Inventory.Backpack()

    @staticmethod
    def update_stats(player):
        """
        Update stats by certain amount
        :param player: player instance
        """

        Player.max_health += int(player.stats['CON']['Value'] ** 1.99)
        Player.health = Player.max_health
        Player.projectileSpeed += int(player.stats['AGL']['Value'] ** 0.01)
        Player.attackCooldown -= int(player.stats['DEX']['Value'] ** 1.01)
        Player.moveSpeed += int(player.stats['AGL']['Value'] ** 0.001)
        Player.baseDamage += int(player.stats['STR']['Value'] ** 0.5)
        Player.healthBar.max_health = Player.max_health
        Player.healthBar.health = Player.health
        Player.healthBar.colour = Helper.WHITE

    @staticmethod
    def player_action(player, action):
        """
        =======================================================================
        Parses player action and fires off appropriate function.
        :param player: instance of the player
        :param action: action to be performed
        =======================================================================
        """

        if not Player.isLeavingRoom:
            if 'move' in action and not player.inventoryIsOpen:
                Player.player_move(action, player)
            elif 'inv' in action:
                Player.inventory_update(action)
            elif 'idle' in action:
                pass
            elif 'attack' in action \
                    and not player.inventoryIsOpen \
                    and not player.is_moving \
                    and pygame.time.get_ticks() \
                    - Player.lastAttack \
                    > Player.attackCooldown:
                Player.attack()
        else:
            Player.leave_room(player)

    @staticmethod
    def leave_room(player):
        """
        =======================================================================
        Function for initiating departure from room
        :param player: player instance
        =======================================================================
        """

        if player.currentLane == -1:
            direction = 'move_right'
        elif player.currentLane == 1:
            direction = 'move_left'
        else:
            direction = None

        if not Player.isLeavingRoom:
            Player.isLeavingRoom = True
        elif player.is_moving:
            Player.player_move(Player.move_direction, player)

        # case for starting movement towards middle lane
        if direction and not player.is_moving:
            Player.player_move(direction, player)
        # once on the middle lane, proceed to go up
        else:
            pass

    @staticmethod
    def attack():
        """
        Generate projectile.
        :return:
        """
        Player.lastAttack = pygame.time.get_ticks()
        Projectile.PlayerProjectile(Player.currentLane)

    @staticmethod
    def inventory_update(action):
        """
        Update inventory states and actions.
        :param action: action as a string i.e. 'switch_inv'
        """
        if 'switch_inv' == action:
            Player.inventoryIsOpen = not Player.inventoryIsOpen
        elif 'open_inv' == action:
            Player.inventoryIsOpen = True
        elif 'close_inv' == action:
            Player.inventoryIsOpen = False

    @staticmethod
    def player_move(direction, player):
        """
        Used for moving player upon swipe input, in future
        will be used for moving from room to room also.

        Args:
            direction -- string of the direction to move
            player -- this player class
        """
        if not player.is_moving:
            if direction == 'move_right' and player.currentLane < 1:
                player.currentLane += 1
                player.move_direction = direction
                player.player_destination = player.playerPos[0]\
                    + player.moveDistance
                player.is_moving = True
            elif direction == 'move_left' and player.currentLane > -1:
                player.currentLane -= 1
                player.move_direction = direction
                player.player_destination = player.playerPos[0] -\
                    player.moveDistance
                player.is_moving = True

        if player.is_moving and player.move_direction == 'move_right':
            if player.playerPos[0] < player.player_destination \
                    and\
                    not player.inventoryIsOpen:
                player.playerPos[0] += Player.moveSpeed
                player.playerRect.x += Player.moveSpeed
            else:
                player.direction = ''
                player.move_direction = ''
                player.is_moving = False

        if player.is_moving and player.move_direction == 'move_left':
            if player.playerPos[0] > player.player_destination \
                    and\
                    not player.inventoryIsOpen:
                player.playerPos[0] -= Player.moveSpeed
                player.playerRect.x -= Player.moveSpeed
            else:
                player.direction = ''
                player.move_direction = ''
                player.is_moving = False

    @staticmethod
    def is_hit(damage):
        """
        Subtract damage from the player's HP.
        :param damage: amount to subtract
        """
        Player.health -= damage
        if Player.health <= 0:
            Player.die()

    @staticmethod
    def level_up():
        """
        Level up player.
        """
        Player.playerInstance.level += 1
        for stat_key in Player.playerInstance.stats.keys():
            Player.playerInstance.stats[stat_key]['Value'] += \
                                            random.randint(0, 1)
        Player.update_stats(Player.playerInstance)

    @staticmethod
    def gain_exp(amount):
        """
        Increase player's experience points by amount and possibly level up.
        :param amount: amount of experience points
        """
        while Player.playerInstance.exp + amount >= \
                Player.playerInstance.exp_to_level_up:
            amount = Player.playerInstance.exp + amount - \
                     Player.playerInstance.exp_to_level_up
            Player.playerInstance.exp = 0
            Player.playerInstance.exp_to_level_up += \
                int(Helper.EXP_REQUIRED ** 0.95)
            Player.playerInstance.level_up()
        Player.playerInstance.exp += amount

    @staticmethod
    def equip(weapon):
        """
        Equip weapon.
        :param weapon: weapon to equip.
        """
        Inventory.Backpack.switch_item(weapon, Player.weaponEquipped)

    @staticmethod
    def die():
        """
        Prepare player for removal.
        """
        Player.is_dead = True
