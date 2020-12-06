import math

with open("input.txt", "r") as f:
    grid = [l.strip() for l in f.readlines()]

height, width = len(grid), len(grid[0])

num_trees_slopes = []
for slope_x, slope_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x, y = slope_x, slope_y
    num_trees = 0
    while y < height:
        if grid[y][x % width] == "#":
            num_trees += 1
        x += slope_x
        y += slope_y
    num_trees_slopes.append(num_trees)

print(math.prod(num_trees_slopes))
