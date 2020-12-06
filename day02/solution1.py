with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

num_correct = 0
for l in lines:
    policy, password = l.split(": ")
    num_occurrences, letter = policy.split(" ")
    low, high = [int(i) for i in num_occurrences.split("-")]
    if low <= password.count(letter) <= high:
        num_correct += 1
print(num_correct)
