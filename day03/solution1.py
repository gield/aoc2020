with open("input.txt", "r") as f:
    grid = [l.strip() for l in f.readlines()]

height, width = len(grid), len(grid[0])
x, y = 3, 1
num_trees = 0
while y < height:
    if grid[y][x % width] == "#":
        num_trees += 1
    x += 3
    y += 1

print(num_trees)
