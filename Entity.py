import pygame
import random
import ImageFiles
import Helper
import copy
from Helper import HEALTH_BAR_THRESHOLDS as THRESHOLDS
from Helper import HEALTH_BAR_COLOURS as COLOURS
import Projectile
import TimeOfDay
# Classes used by Entity type Objects

pygame.init()

# Contains all enemies that are currently being displayed
enemy_list = []

health_bars = []


class HealthBar:

    def __init__(self, entity):
        self.size = [entity.sprite.get_width()
                     if type(entity) == Enemy
                     else entity.playerSurf.get_width(),
                     Helper.HEALTH_BAR_SIZE[1]]
        self.max_health = entity.health
        self.health = self.max_health
        self.parent = entity
        self.colour = COLOURS[len(COLOURS) - 1]
        self.pos = [0, 0]
        self.pos[0] = entity.pos[0] \
            if type(entity) == Enemy \
            else entity.playerPos[0]
        self.pos[1] = entity.pos[1] + int(entity.rect.height) \
            if type(entity) == Enemy \
            else entity.playerPos[1]

        health_bars.append(self)

    def colour_update(self):
        if self.health <= 0:
            health_bars.remove(self)
        for i in range(0, len(THRESHOLDS)):
            if self.health <= int(self.max_health * THRESHOLDS[i]):
                self.colour = COLOURS[i]
                return

    def health_bar_update(self):
        self.health = self.parent.health
        self.pos[0] = self.parent.pos[0] \
            if type(self.parent) == Enemy \
            else self.parent.playerPos[0]
        self.pos[1] = self.parent.pos[1] + int(self.parent.rect.height) \
            if type(self.parent) == Enemy \
            else self.parent.playerPos[1] - 10
        if self.parent.health < self.max_health:
            self.colour_update()


class Entity:
    """
    ---------------------------------------------------------------------------
    Super class for all entities. It should never be used directly,
        only extended from.
    ---------------------------------------------------------------------------
    """

    # index is used to keep track of entities
    entity_index = 0  # Declaration of static Index
    # Declaration of static alignment for all Entities
    entity_alignment = ('Aggressive', 'Passive', 'Friendly')
    defaultHealth = 100

    def __init__(self):
        # subname is a unique identifier that uses the index
        self.subname = 'Entity' + str(Entity.entity_index)

        # name for flavour
        self.name = 'Placeholder name'

        # Importing index into the Entity-specific variable
        self.index = Entity.entity_index

        # Incrementing the index of all entities
        Entity.entity_index += 1

        # defining where the entity is encountered (by default, nowhere)
        self.on_encounter = False
        self.on_battle = False

        # level of entity
        self.level = 1

        # setting alignment to passive as a default
        self.alignment = Entity.entity_alignment[1]

        # setting all stats to the default values from the Helper
        self.stats = copy.deepcopy(Helper.STATS)

        # To do: define states, as to specify what
        # images and animations to incorporate into lists


class Enemy(Entity):
    """
    ---------------------------------------------------------------------------
    Enemy class. Used for creating entities that attack the player regularly.
    Their stats increase along with the room they are in
    ---------------------------------------------------------------------------
    """

    numberOfOnscreenEnemies = 0

    def __init__(self, room=None):
        Entity.__init__(self)

        if room is None:
            raise(ValueError, 'Room not specified for enemy')

        self.on_battle = True
        self.room = room

        self.level = random.randint(max(1, room.index - 5), room.index + 1)

        for stat_key in self.stats.keys():
            self.stats[stat_key]['Value'] += random.randint(
                min(self.level, room.index),
                max(self.level, room.index))

        self.alignment = Entity.entity_alignment[0]

        self.health = self.stats['CON']['Value'] * 10 + 5 * self.level

        self.sprite = ImageFiles.images['Enemy']  # [random.randint(0, len(ImageFiles.images) - 1)]

        self.chance_to_attack = 10 + 5 * self.stats['DEX']['Value']

        self.last_attack = pygame.time.get_ticks()

        self.attack_cooldown = \
            random.randint(300, 500) - int(self.stats['DEX']['Value'] ** 1.1)

        self.max_attack_chance = 1000

        lane_is_occupied = True
        self.lane_key = 'middle'

        self.base_damage = self.stats['STR']['Value']

        self.damage = self.calculate_damage

        self.rect = self.sprite.get_rect()

        while lane_is_occupied:
            self.lane_key = random.choice(list(Helper.LANES))
            lane_is_occupied = Helper.LANES[self.lane_key][1]

        Helper.LANES[self.lane_key][1] = True
        self.pos = [
                    Helper.LANES[self.lane_key][0][0] - int(
                                                self.sprite.get_width() / 2
                                                            ),
                    Helper.LANES[self.lane_key][0][1] - int(
                                                self.sprite.get_height() / 2
                                                            )
                    ]
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        Enemy.numberOfOnscreenEnemies += 1

        self.healthBar = HealthBar(self)

    def calculate_damage(self):
        """
        =======================================================================
        Returns damage to enemy based on time of day.

        :return: damage to enemy
        =======================================================================
        """
        return self.base_damage\
            * TimeOfDay.TimeOfDay.MonsterBuff\
            * int(self.stats['STR']['Value'] ** 1.3)

    def is_hit(self, damage):
        """
        =======================================================================
        Calculate health loss and death.

        :param damage: amount of damage for the enemy to take
        =======================================================================
        """
        self.health = self.health - damage
        # print('\'tis a hit: ' + str(self.health) + ' hp remaining')
        # play_sound(enemy_hit)
        if self.health <= 0:
            Projectile.PlayerProjectile.grant_exp(100 * self.level)
            self.__del__()

    def enemy_attack(self):
        """
        =======================================================================
        Randomly (within range) determine whether enemy should attack.
        =======================================================================
        """
        attack = random.randint(1, self.max_attack_chance)
        if attack <= self.chance_to_attack \
                and pygame.time.get_ticks()\
                - self.last_attack \
                > self.attack_cooldown:
            Projectile.EnemyProjectile(self.lane_key, self)
            self.last_attack = pygame.time.get_ticks()

    def __del__(self):
        """
        =======================================================================
        Deletes enemy instance, and lowers number of onscreen enemies.
        =======================================================================
        """
        for projectile in Projectile.attackSprites:
            if projectile.parent == self:
                Projectile.attackSprites.remove(projectile)
        Helper.LANES[self.lane_key][1] = False
        Enemy.numberOfOnscreenEnemies = \
            max(0, Enemy.numberOfOnscreenEnemies - 1)
        if self in enemy_list:
            enemy_list.remove(self)
        else:
            del self
