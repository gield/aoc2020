with open("input.txt", "r") as f:
    groups = [g.strip() for g in f.read().split("\n\n")]

print(sum(1 for g in groups for c in set(g.replace("\n", "")) if all(c in l for l in g.split("\n"))))
