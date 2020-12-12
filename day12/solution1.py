with open("input.txt", "r") as f:
    instructions = [(l[0], int(l[1:])) for l in f.readlines()]


def rotate(dx, dy, degrees):
    num_turns = (degrees / 90) % 4
    while num_turns:
        dx, dy = dy, -dx
        num_turns -= 1
    return dx, dy


x, y = 0, 0
dx, dy = 1, 0
for action, value in instructions:
    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x -= value
    elif action == "L":
        dx, dy = rotate(dx, dy, -value)
    elif action == "R":
        dx, dy = rotate(dx, dy, value)
    elif action == "F":
        x += value * dx
        y += value * dy

print(abs(x) + abs(y))
