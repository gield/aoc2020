import re
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


def get_dx_dy(direction: str):
    if direction == "e":
        return 1, 0
    elif direction == "se":
        return 1, -1
    elif direction == "sw":
        return 0, -1
    elif direction == "w":
        return -1, 0
    elif direction == "nw":
        return -1, 1
    elif direction == "ne":
        return 0, 1


hex_grid = defaultdict(lambda: False)  # white is False
for line in lines:
    x, y = 0, 0
    directions = re.findall(r"(e|ne|nw|w|sw|se)", line)
    for direction in directions:
        dx, dy = get_dx_dy(direction)
        x += dx
        y += dy
    hex_grid[x, y] = not hex_grid[x, y]

print(sum(hex_grid.values()))
