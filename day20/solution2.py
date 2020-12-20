import numpy as np

with open("input.txt", "r") as f:
    raw_tiles = [t.strip().split("\n") for t in f.read().split("\n\n")]

tiles = {}
for raw_tile in raw_tiles:
    n = int(raw_tile[0][5:-1])
    tile = [list(map(int, l.replace("#", "1").replace(".", "0"))) for l in raw_tile[1:]]
    tiles[n] = np.array(tile)

num_rows = num_cols = int(np.sqrt(len(tiles)))


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


# Find all permutations for all tiles (bit of dynamic programming)
permutations = {n: list(get_permutations(tiles[n])) for n in tiles.keys()}

# Find the number of fitting sides per tile
num_fitting_sides = {}
for n, tile in tiles.items():
    num_fitting_sides[n] = 0
    relevant_permutations = [p
                             for current_n, current_permutations in permutations.items()
                             for p in current_permutations
                             if current_n != n]
    if any(is_tile1_above_tile2(tile, p) for p in relevant_permutations):
        num_fitting_sides[n] += 1
    if any(is_tile1_above_tile2(p, tile) for p in relevant_permutations):
        num_fitting_sides[n] += 1
    if any(is_tile1_left_of_tile2(tile, p) for p in relevant_permutations):
        num_fitting_sides[n] += 1
    if any(is_tile1_left_of_tile2(p, tile) for p in relevant_permutations):
        num_fitting_sides[n] += 1

# Find a candidate for the top-left tile
# This can be any of the tiles with only 2 fitting sides
top_left_tile_n = next(n for n, num_sides in num_fitting_sides.items() if num_sides == 2)

# Find the permutation of the top-left tile where it fits in the top-left corner
# Note: there are 2 possible permutations where this is true, we only need 1
for top_left_permutation in permutations[top_left_tile_n]:
    for n, tile in tiles.items():
        relevant_permutations = [p
                                 for current_n, current_permutations in permutations.items()
                                 for p in current_permutations
                                 if current_n != top_left_tile_n]
        if any(is_tile1_above_tile2(p, top_left_permutation) for p in relevant_permutations):
            break
        if any(is_tile1_left_of_tile2(p, top_left_permutation) for p in relevant_permutations):
            break
    else:
        top_left_tile = top_left_permutation
        break  # There are actually 2 possibilities, we only need 1

# Lay the actual puzzle
image_n = {}
image_n[(0, 0)] = top_left_tile_n
image_tiles = {}
image_tiles[(0, 0)] = top_left_tile
for row in range(num_rows):
    for col in range(num_cols):
        if row == 0 and col == 0:
            continue
        num_sides_needed = 4
        if row == 0 or row == num_rows - 1:
            num_sides_needed -= 1
        if col == 0 or col == num_cols - 1:
            num_sides_needed -= 1
        possible_tiles = {n
                          for n, num_sides in num_fitting_sides.items()
                          if num_sides == num_sides_needed and n not in image_n.values()}
        for tile_n in possible_tiles:
            for p in permutations[tile_n]:
                if col > 0:
                    tile = image_tiles[(row, col - 1)]
                    if is_tile1_left_of_tile2(tile, p):
                        image_n[(row, col)] = tile_n
                        image_tiles[(row, col)] = p
                else:
                    tile = image_tiles[(row - 1, col)]
                    if is_tile1_above_tile2(tile, p):
                        image_n[(row, col)] = tile_n
                        image_tiles[(row, col)] = p

# Remove the borders of each tile and remove the gaps
new_rows = []
for row in range(num_rows):
    new_columns = []
    for col in range(num_cols):
        tile = image_tiles[(row, col)]
        new_columns.append(tile[1:-1, 1:-1])  # type: ignore
    new_rows.append(np.hstack(new_columns))
image = np.vstack(new_rows)

# Put the sea monster into nice coordinates: as seen from (1, 0)
sea_monster_str = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")[1:]  # noqa: W291

base_row, base_col = 1, 0
sea_monster_coordinates = []
for row in range(3):
    for col in range(len(sea_monster_str[0])):
        if sea_monster_str[row][col] == "#":
            sea_monster_coordinates.append((row - base_row, col - base_col))

# Actually find the sea monster in the image
num_rows, num_cols = image.shape
for image_permutation in get_permutations(image):
    num_sea_monsters_found = 0
    image_permutation_found = image_permutation.copy()
    for row in range(num_rows):
        for col in range(num_cols):
            for sm_row, sm_col in sea_monster_coordinates:
                new_row, new_col = row + sm_row, col + sm_col
                if not 0 <= new_row < num_rows or not 0 <= new_col < num_cols:
                    break
                if image_permutation[new_row, new_col] != 1:
                    break
            else:
                num_sea_monsters_found += 1
                for sm_row, sm_col in sea_monster_coordinates:
                    new_row, new_col = row + sm_row, col + sm_col
                    image_permutation_found[new_row, new_col] = 2
    if num_sea_monsters_found > 0:
        print((image_permutation_found == 1).sum())
