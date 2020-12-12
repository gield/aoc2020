with open("input.txt", "r") as f:
    instructions = [(l[0], int(l[1:])) for l in f.readlines()]


def rotate(wx, wy, degrees):
    num_turns = (degrees / 90) % 4
    while num_turns:
        wx, wy = wy, -wx
        num_turns -= 1
    return wx, wy


x, y = 0, 0
wx, wy = 10, 1
for action, value in instructions:
    if action == "N":
        wy += value
    elif action == "S":
        wy -= value
    elif action == "E":
        wx += value
    elif action == "W":
        wx -= value
    elif action == "L":
        wx, wy = rotate(wx, wy, -value)
    elif action == "R":
        wx, wy = rotate(wx, wy, value)
    elif action == "F":
        x += value * wx
        y += value * wy

print(abs(x) + abs(y))
