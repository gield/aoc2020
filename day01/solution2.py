with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

numbers = [int(l) for l in lines]
for i in range(len(numbers) - 2):
    for j in range(i, len(numbers) - 1):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
