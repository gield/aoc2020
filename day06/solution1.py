with open("input.txt", "r") as f:
    groups = [g.strip() for g in f.read().split("\n\n")]

print(sum(len(set(g.replace("\n", ""))) for g in groups))
