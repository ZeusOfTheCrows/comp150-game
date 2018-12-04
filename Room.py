import ImageFiles
import random
import Helper


class Room:
    """
    ---------------------------------------------------------------------------
    Class used by Room type Objects. Contains functions for changing room.
    ---------------------------------------------------------------------------
    """
    rooms_index = 0
    rooms_list = []     # should usually contain 3 rooms

    prev_room = None
    current_room = None
    next_room = None

    number_of_steps = 100
    room_move_speed = int(Helper.RESOLUTION[1] / number_of_steps)  # pixels/sec

    next_room_x = -Helper.RESOLUTION[1]
    current_room_x = 0
    prev_room_x = Helper.RESOLUTION[1]

    @staticmethod
    def reset_room():
        Room.rooms_index = 0
        Room.rooms_list = []  # should usually contain 3 rooms tops

        Room.prev_room = None
        Room.current_room = None
        Room.next_room = None

    def __init__(self):
        self.index = Room.rooms_index
        Room.rooms_list.append(self)
        Room.rooms_index += 1

        self.position = [0, 0]

        self.prev = None
        self.next = None

        self.is_populated = False

        self.texture = random.choice(list(ImageFiles.images['Rooms'].values()))

        if self.index == 0:
            Room.current_room = self
            # Currently a single room is available
        else:
            Room.rooms_list[1].next = self
            self.prev = Room.rooms_list[1]
            self.position[1] = Room.next_room_x
            Room.next_room = self

    @staticmethod
    def remove_prev_room():
        """
        =======================================================================
        Simple function to remove the previous room.
        =======================================================================
        """

        Room.prev_room = None
        del Room.rooms_list[0]

    @staticmethod
    def advance_room():
        """
        =======================================================================
        Simple function to advance to the next room.
        =======================================================================
        """

        if Room.prev_room:
            Room.remove_prev_room()
        Room.prev_room = Room.current_room
        Room.prev_room.position[1] -= Room.room_move_speed
        Room.current_room = Room.next_room
        Room.current_room.position[1] -= Room.room_move_speed
        Room.next_room = Room()

    @staticmethod
    def move_room():
        """
        =======================================================================
        Simple function to animate moving to the next room.
        =======================================================================
        """

        if Room.current_room.position[1] < Room.current_room_x:
            Room.current_room.position[1] += Room.room_move_speed
        if Room.prev_room:
            if Room.prev_room.position[1] < Room.prev_room_x:
                Room.prev_room.position[1] += Room.room_move_speed

