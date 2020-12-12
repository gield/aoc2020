from enum import Enum

with open("input.txt", "r") as f:
    instructions = [(l[0], int(l[1:])) for l in f.readlines()]


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def turn(self, degrees):
        num_turns = degrees / 90
        return Direction((self.value + num_turns) % 4)


x, y = 0, 0
direction = Direction.EAST
for action, value in instructions:
    if action == "F":
        action = direction.name[0]  # e.g. EAST becomes E
    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x -= value
    elif action == "L":
        direction = direction.turn(-value)
    elif action == "R":
        direction = direction.turn(value)

print(abs(x) + abs(y))
