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

    currentLane = 0  # 0: Middle, -1: Left, 1: Right
    displaySurface = Helper.DISPLAY_SURFACE
    playerSurf = ImageFiles.images['Player']
    playerRect = playerSurf.get_rect()
    playerPos = [Helper.RESOLUTION[0] * 0.5 - playerSurf.get_width() * 0.5,
                 Helper.RESOLUTION[1] * 0.2 - playerSurf.get_height() * 0.5
                 + 600
                 ]
    playerRect.x = playerPos[0]
    playerRect.y = playerPos[1]
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
    player_destination = 0

    def __init__(self):
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
        Player.max_health += int(player.stats['CON']['Value'] ** 1.99)
        Player.health = Player.max_health
        Player.projectileSpeed += int(player.stats['AGL']['Value'] ** 0.01)
        Player.attackCooldown -= int(player.stats['DEX']['Value'] ** 1.01)
        Player.moveSpeed += int(player.stats['AGL']['Value'] ** 0.001)
        Player.baseDamage += int(player.stats['STR']['Value'] ** 0.5)
        del Player.healthBar
        Player.healthBar = Entity.HealthBar(Player)

    @staticmethod
    def player_action(player, action):
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
        Player.lastAttack = pygame.time.get_ticks()
        Projectile.PlayerProjectile(Player.currentLane)

    @staticmethod
    def inventory_update(action):
        if 'switch_inv' == action:
            Player.inventoryIsOpen = not Player.inventoryIsOpen
        elif 'open_inv' == action:
            Player.inventoryIsOpen = True
        elif 'close_inv' == action:
            Player.inventoryIsOpen = False

    @staticmethod
    def player_move(direction, player):  # needs four directions
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
        Player.health -= damage
        if Player.health <= 0:
            Player.die()

    @staticmethod
    def level_up():
        Player.playerInstance.level += 1
        for stat_key in Player.playerInstance.stats.keys():
            Player.playerInstance.stats[stat_key]['Value'] += \
                                            random.randint(0, 1)
        Player.update_stats(Player.playerInstance)

    @staticmethod
    def gain_exp(amount):
        while Player.playerInstance.exp + amount >= \
                Player.playerInstance.exp_to_level_up:
            amount = Player.playerInstance.exp + amount - \
                     Player.playerInstance.exp_to_level_up
            Player.playerInstance.exp = 0
            Player.playerInstance.exp_to_level_up += \
                int(Helper.EXP_REQUIRED ** 0.95)
            Player.playerInstance.level_up()

    @staticmethod
    def equip(weapon):
        Inventory.Backpack.switch_item(weapon, Player.weaponEquipped)

    @staticmethod
    def die():
        Player.is_dead = True
