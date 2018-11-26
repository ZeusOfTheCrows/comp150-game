import random
import pygame
import Helper
import Entity
import ImageFiles

# Classes used by Room type Objects


class Room:
    """
    Base class for all rooms, all other rooms should inherit from this.
    """
    room_index = 0

    # create dictionary for lane positions

    def __init__(self):
        self.index = Room.room_index
        Room.room_index += 1


class RoomTutorial(Room):
    """
    Tutorial room, will be scripted rather than randomised
    """
    current_stage = 0
    tutorial_stages = 3
    prevRoom = None
    nextRoom = None

    def __init__(self, pos_x, pos_y):
        if RoomTutorial.current_stage <= RoomTutorial.tutorial_stages:
            # add code for room transition
            Room.__init__(self)
            RoomTutorial.current_stage += 1

            self.texture = ImageFiles.images['Rooms']['Tutorial']
            self.pos = []
            self.pos[0] = pos_x
            self.pos[1] = pos_y

            # Use this in the regular enemy and boss rooms
            self.lanes = dict()
            self.lanes['left'] = Lane(150, 150, 'left')
            self.lanes['centre'] = Lane(375, 150, 'centre')
            self.lanes['right'] = Lane(600, 150, 'right')
        else:
            # add code for completing tutorial
            pass

    @staticmethod
    def create_tutorial_room(enemies=random.randint(1, 3)):
        """
        Paul can write this when he wants to die less
        :param enemies: Number of enemies to generate. Can be specified
                                manually, will be randomised otherwise.
        :return:
        """
        room = RoomTutorial()

        if enemies > 0:
            room.lanes['centre'].occupy_lane(Entity.Enemy)
            enemies -= 1

        if enemies > 0:
            room.lanes['left'].occupy_lane(Entity.Enemy)
            enemies -= 1

        if enemies > 0:
            room.lanes['right'].occupy_lane(Entity.Enemy)
            enemies -= 1


class Lane:
    """Legacy, to be purged."""
    def __init__(self, origin_x, origin_y, key, is_occupied=False):
        self.occupied = is_occupied
        self.occupant = None
        self.origin = (origin_x, origin_y)
        self.key = key

    def occupy_lane(self, occupant):
        self.occupant = occupant
        self.occupied = True


class RoomEncounter(Room):
    """
    Room with an encounter, will be used later.
    """
    def __init__(self, room_type=random.randint(1, 4)):
        Room.__init__(self)


class RoomEnemy(Room):
    """
    Most used room, normal room with enemies in.
    """
    def __init__(self):
        Room.__init__(self)


class RoomBoss(Room):
    """Boss room, will be a room with a boss."""
    def __init__(self):
        Room.__init__(self)

