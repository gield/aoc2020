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

all_dx_dy = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
for day in range(100):
    # Make sure all neighbors are visited at least once
    for x, y in list(hex_grid.keys()):
        for dx, dy in all_dx_dy:
            hex_grid[x + dx, y + dy]
    new_hex_grid = hex_grid.copy()
    for (x, y), color in list(hex_grid.items()):
        num_black = sum(hex_grid[x + dx, y + dy] for dx, dy in all_dx_dy)
        if color and num_black in {0, 3, 4, 5, 6}:
            new_hex_grid[x, y] = False
        if not color and num_black == 2:
            new_hex_grid[x, y] = True
    hex_grid = new_hex_grid

print(sum(hex_grid.values()))
