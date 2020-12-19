from collections import defaultdict
import itertools

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


def mask_value(mask, value):
    # First, apply the "1" bitmask bits
    for i, c in enumerate(mask[::-1]):
        if c == "1":
            n = 2 ** i
            # Set bit to 1 by toggling if 0
            if not value & n:
                value = value ^ n

    # Then, find all floating values
    floating_values = []
    for i, c in enumerate(mask[::-1]):
        if c == "X":
            floating_values.append(2 ** i)

    # Finally, yield all possible values by toggling bits
    for possibilities in itertools.product([0, 1], repeat=len(floating_values)):
        possible_value = value
        for i, p in enumerate(possibilities):
            if p == 1:
                possible_value = possible_value ^ floating_values[i]
        yield possible_value


mem = defaultdict(lambda: 0)
mask = None
for line in lines:
    if line.startswith("mask = "):
        mask = line[7:]
    else:
        mem_location, number = [int(i) for i in line[4:].split("] = ")]
        for floating_mem_location in mask_value(mask, mem_location):
            mem[floating_mem_location] = number

print(sum(mem.values()))
