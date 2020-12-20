import itertools
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

pocket_dimension = defaultdict(lambda: False)
for row in range(len(lines)):
    for col in range(len(lines[0])):
        pocket_dimension[(row, col, 0, 0)] = (lines[row][col] == "#")


def get_neighbors(x, y, z, w):
    for dx, dy, dz, dw in itertools.product([-1, 0, 1], repeat=4):
        if (dx, dy, dz, dw) != (0, 0, 0, 0):
            yield x + dx, y + dy, z + dz, w + dw


for cycle in range(6):
    # Make sure that every neighbor is in the defaultdict
    for current in list(pocket_dimension.keys()):
        for neighbor in get_neighbors(*current):
            pocket_dimension[neighbor]
    # Create the new pocket dimension
    new_pocket_dimension = pocket_dimension.copy()
    for current, state in list(pocket_dimension.items()):
        num_active_neighbors = sum(pocket_dimension[neighbor] for neighbor in get_neighbors(*current))
        if state and num_active_neighbors not in {2, 3}:
            new_pocket_dimension[current] = False
        if not state and num_active_neighbors == 3:
            new_pocket_dimension[current] = True
    # The new pocket dimension becomes the current pocket dimension
    pocket_dimension = new_pocket_dimension

print(sum(pocket_dimension.values()))
