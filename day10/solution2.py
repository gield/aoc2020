from collections import defaultdict

with open("input.txt", "r") as f:
    numbers = [int(l.strip()) for l in f.readlines()]

aim = max(numbers) + 3
numbers = [0] + sorted(numbers) + [aim]

memo = defaultdict(lambda: 0)  # why do I keep calling this memo?!
memo[len(numbers) - 1] = 1
for n in range(len(numbers) - 1, -1, -1):  # N-1 --> 0
    for i in range(n + 1, len(numbers)):
        if numbers[i] - numbers[n] <= 3:
            memo[n] += memo[i]
        else:
            break
print(memo[0])
