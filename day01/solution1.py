with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

numbers = [int(l) for l in lines]
for i in range(len(numbers)-1):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i] * numbers[j])