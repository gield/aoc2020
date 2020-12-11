from collections import defaultdict

with open("input.txt", "r") as f:
    raw_grid = [l.strip() for l in f.readlines()]

height, width = len(raw_grid), len(raw_grid[0])
grid = defaultdict(lambda: ".")
for y in range(height):
    for x in range(width):
        grid[(y, x)] = raw_grid[y][x]


def get_num_occupied(grid, y, x):
    num_occupied = 0
    for dx, dy in {(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)}:
        for i in range(1, height):
            if not 0 <= y + i * dy < height or not 0 <= x + i * dx < width:
                break
            if grid[(y + i * dy, x + i * dx)] == "#":
                num_occupied += 1
                break
            if grid[(y + i * dy, x + i * dx)] == "L":
                break
    return num_occupied


def step(grid):
    new_grid = grid.copy()
    for y in range(height):
        for x in range(width):
            if grid[(y, x)] == "L" and get_num_occupied(grid, y, x) == 0:
                new_grid[(y, x)] = "#"
            elif grid[(y, x)] == "#" and get_num_occupied(grid, y, x) >= 5:
                new_grid[(y, x)] = "L"
    return new_grid


while True:
    next_grid = step(grid)
    if grid == next_grid:
        break
    grid = next_grid

print(list(grid.values()).count("#"))
