with open("input.txt", "r") as f:
    groups = [g.strip() for g in f.read().split("\n\n")]

num = 0
for g in groups:
    lines = g.split("\n")
    for c in set(g.replace("\n", "")):
        if all(c in l for l in lines):
            num += 1
print(num)
