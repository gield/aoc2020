from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


def mask_value(mask, value):
    for i, c in enumerate(mask[::-1]):
        if c == "1":
            n = 2 ** i
            # Set bit to 1 by toggling if 0
            if not value & n:
                value = value ^ n
        elif c == "0":
            n = 2 ** i
            # Set bit to 0 by toggling if 1
            if value & n:
                value = value ^ n
    return value


mem = defaultdict(lambda: 0)
mask = None
for line in lines:
    if line.startswith("mask = "):
        mask = line[7:]
    else:
        mem_location, number = [int(i) for i in line[4:].split("] = ")]
        mem[mem_location] = mask_value(mask, number)

print(sum(mem.values()))
