from ps2 import Position, RectangularRoom, StandardRobot
import random
random.seed(0)

width = 5
height = 5
room = RectangularRoom(width, height)


def show_tiles(room):
    for k, v in room.tiles.items():
        print(k, v)


def cleanAll(room):
    for tile in room.tiles:
        room.tiles[tile] = 1


def getDirty(room):
    for tile in room.tiles:
        room.tiles[tile] = 0

show_tiles(room)
cleanAll(room)
show_tiles(room)
getDirty(room)
show_tiles(room)
