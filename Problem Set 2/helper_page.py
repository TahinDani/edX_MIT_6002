from ps2 import Position, RectangularRoom, StandardRobot
import random
random.seed(0)

width = 5
height = 5

room = RectangularRoom(width, height)
#myPos = Position(2, 2)
#print(myPos)
#room.cleanTileAtPosition(myPos)
for k, v in room.tiles.items():
    print(k, v)

def cleanAll(room):
    for tile in room.tiles:
        room.tiles[tile] = 1

cleanAll(room)
for k, v in room.tiles.items():
    print(k, v)

def getDirty(room):
    for tile in room.tiles:
        room.tiles[tile] = 0

getDirty(room)

for k, v in room.tiles.items():
    print(k, v)
