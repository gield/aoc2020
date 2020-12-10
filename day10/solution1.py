with open("input.txt", "r") as f:
    numbers = [int(l.strip()) for l in f.readlines()]

aim = max(numbers) + 3
numbers = [0] + sorted(numbers) + [aim]
num_1_step, num_3_step = 0, 0
for n in sorted(numbers):
    joltage = num_1_step + 3 * num_3_step
    if n - joltage == 1:
        num_1_step += 1
    elif n - joltage == 3:
        num_3_step += 1

print(num_1_step * num_3_step)
