import numpy as np

with open("input.txt", "r") as f:
    raw_tiles = [t.strip().split("\n") for t in f.read().split("\n\n")]

tiles = {}
for raw_tile in raw_tiles:
    n = int(raw_tile[0][5:-1])
    tile = [list(map(int, l.replace("#", "1").replace(".", "0"))) for l in raw_tile[1:]]
    tiles[n] = np.array(tile)


def print_tile(tile):
    for row in range(tile.shape[0]):
        for col in tile[row]:
            print(f"{'#' if col == 1 else '.'}", end="")
        print()


def is_tile1_above_tile2(tile1, tile2):
    return np.all(tile1[-1] == tile2[0])


def is_tile1_left_of_tile2(tile1, tile2):
    return np.all(tile1[:, -1] == tile2[:, 0])


def get_permutations(tile):
    for k in range(4):
        rotated_tile = np.rot90(tile, k=k)
        yield rotated_tile
        yield np.flipud(rotated_tile)


permutations = {n: list(get_permutations(tiles[n])) for n in tiles.keys()}

solution = 1
for n, tile in tiles.items():
    num_fitting_sides = 0
    relevant_permutations = [p
                             for current_n, current_permutations in permutations.items()
                             for p in current_permutations
                             if current_n != n]
    if any(is_tile1_above_tile2(tile, p) for p in relevant_permutations):
        num_fitting_sides += 1
    if any(is_tile1_above_tile2(p, tile) for p in relevant_permutations):
        num_fitting_sides += 1
    if any(is_tile1_left_of_tile2(tile, p) for p in relevant_permutations):
        num_fitting_sides += 1
    if any(is_tile1_left_of_tile2(p, tile) for p in relevant_permutations):
        num_fitting_sides += 1
    if num_fitting_sides == 2:
        solution *= n
print(solution)
