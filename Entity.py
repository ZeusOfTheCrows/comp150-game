import pygame
import random
import ImageFiles
import Helper
# Classes used by Entity type Objects


pygame.init()
'''
windowHeight = 150
windowWidth = 450

screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
'''

enemy_list = []

class Entity:
    # index is used to keep track of entities
    entity_index = 0  # Declaration of static Index
    # Declaration of static alignment for all Entities
    entity_alignment = ('Aggressive', 'Passive', 'Friendly')
    defaultHealth = 100

    def __init__(self):
        # subname is a unique identifier that uses the index
        self.subname = 'Entity' + str(Entity.entity_index)
        name = 'Placeholder name'
        # Importing index into the Entity-specific variable
        self.index = Entity.entity_index

        # Incrementing the index of all entities
        Entity.entity_index += 1

        # defining where the entity is encountered (by default, nowhere)
        self.on_encounter = False
        self.on_battle = False

        # setting alignment to passive as a default
        self.alignment = Entity.entity_alignment[1]

        # To do: define states, as to specify what
        # images and animations to incorporate into lists


class Enemy(Entity):

    numberOfOnscreenEnemies = 0

    def __init__(self):
        Entity.__init__(self)
        self.on_battle = True
        self.alignment = Entity.entity_alignment[0]
        self.health = Entity.defaultHealth  # * (enemyLevel * 0.1)
        self.sprite = ImageFiles.images['Enemy']  # [random.randint(0, len(ImageFiles.images) - 1)]

        lane_is_occupied = True
        lane_key = 'middle'

        while lane_is_occupied:
            lane_key = random.choice(list(Helper.LANES))
            lane_is_occupied = Helper.LANES[lane_key][1]

        Helper.LANES[lane_key][1] = True
        self.pos = [
                    Helper.LANES[lane_key][0][0] - int(self.sprite.get_width() / 2),
                    Helper.LANES[lane_key][0][1] - int(self.sprite.get_height() / 2)
                    ]
        Enemy.numberOfOnscreenEnemies += 1

    def is_hit(self, damage):
        self.health = self.health - damage
        # play_sound(enemy_hit)


class EnemyBoss(Enemy):

    def __init__(self):
        Enemy.__init__(self)
