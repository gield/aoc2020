with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

num_correct = 0
for l in lines:
    policy, password = l.split(": ")
    positions, letter = policy.split(" ")
    pos1, pos2 = [int(i) for i in positions.split("-")]
    if (password[pos1 - 1] == letter) != (password[pos2 - 1] == letter):
        num_correct += 1
print(num_correct)
