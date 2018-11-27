import ImageFiles
import random
import Helper

# Classes used by Room type Objects


class Room:
    rooms_index = 0
    rooms_list = []     # should usually contain 3 rooms tops

    prev_room = None
    current_room = None
    next_room = None

    number_of_steps = 100
    room_move_speed = int(Helper.RESOLUTION[1] / number_of_steps)  # pixels/sec

    next_room_x = -Helper.RESOLUTION[1]
    current_room_x = 0
    prev_room_x = Helper.RESOLUTION[1]

    def __init__(self):
        self.index = Room.rooms_index
        Room.rooms_list.append(self)
        Room.rooms_index += 1

        self.position = [0, 0]

        self.prev = None
        self.next = None

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
    def remove_room(room):
        Room.prev_room = None
        del Room.rooms_list[0]

    @staticmethod
    def advance_room():
        # print('Rooms list:', str(Room.rooms_list))
        if Room.prev_room:
            # print('Removing room',str(Room.prev_room))
            Room.remove_room(Room.prev_room)
        Room.prev_room = Room.current_room
        Room.prev_room.position[1] -= Room.room_move_speed
        Room.current_room = Room.next_room
        Room.current_room.position[1] -= Room.room_move_speed
        Room.next_room = Room()     # TODO: initialize here or outside?

    @staticmethod
    def move_room():
        if Room.current_room.position[1] < Room.current_room_x:
            print('Moving next room by', Room.room_move_speed)
            Room.current_room.position[1] += Room.room_move_speed
        if Room.prev_room:
            if Room.prev_room.position[1] < Room.prev_room_x:
                print('Moving current room by', Room.room_move_speed)
                Room.prev_room.position[1] += Room.room_move_speed

