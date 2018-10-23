# Classes used by Entity type Objects
import Helper
import random

class Entity:

    # index is used to keep track of entities
    entity_index = 0    # Declaration of static Index
    entity_alignment = ('Aggressive', 'Passive', 'Friendly')    # Declaration of static alignment for all Entities

    def __init__(self):
        subname = 'Entity' + str(Entity.entity_index)    # subname is a unique identifier that uses the index
        name = 'Placeholder name'
        index = Entity.entity_index     # Importing index into the Entity-specific variable

        Entity.entity_index += 1    # Incrementing the index of all entities

        on_encounter = False    # defining where the entity is encountered (by default, nowhere)
        on_battle = False

        alignment = Entity.entity_alignment[1]  # setting alignment to passive as a default

        # To do: define states, as to specify what images and animations to incorporate into lists


class Player(Entity):

    def __init__(self): # hi
        Entity.__init__(self)


class Enemy(Entity):

    def __init__(self):
        Entity.__init__(self)


class EnemyBoss(Enemy):

    def __init__(self):
        Enemy.__init__(self)

# Classes used by Room type Objects


class Room:

    room_index = 0

    def __init__(self):
        Index = Room.room_index
        Room.room_index += 1


class RoomEncounter(Room):

    def __init__(self):
        Room.__init__(self)


class RoomEnemy(Room):

    def __init__(self):
        Room.__init__(self)


class RoomBoss(Room):

    def __init__(self):
        Room.__init__(self)

# Classes used by Item type Objects


class Item:

    item_index = 0

    def __init__(self):
        index = Item.item_index
        Item.item_index += 1


class Weapon(Item):

    def generate_modifiers(self):
        # modifier array should contain: AFFINITY, ELEMENT, ELEMENT_TIER, BONUS MODIFIER, QUALITY
        # to indicate the lack of a modifier, -1 will be used

        for i in range(1, 5):

            return modifiers

    def generate_name(self, modifiers):
        name = 'GenericItem' + str(Item.item_index)     # Placeholder
        return name

    def __init__(self, isCustom = False):   # If we want to create a custom item, all we have to do is set isCustom to True
        Item.__init__(self)
        if not isCustom:
            modifiers = Weapon.generate_modifiers(self)
        Weapon.generate_name(self, modifiers)
