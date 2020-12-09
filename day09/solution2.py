with open("input.txt", "r") as f:
    numbers = [int(l.strip()) for l in f.readlines()]


def has_sum(n, preamble):
    for i in range(len(preamble) - 1):
        for j in range(i, len(preamble)):
            if preamble[i] + preamble[j] == n:
                return True
    return False


def get_invalid_number(numbers):
    for i in range(25, len(numbers)):
        preamble = numbers[i - 25:i]
        n = numbers[i]
        if not has_sum(n, preamble):
            return n


def get_solution(numbers, invalid_number):
    for c in range(2, len(numbers)):
        for i in range(len(numbers) - c):
            if sum(numbers[i:i + c]) == invalid_number:
                return min(numbers[i:i + c]) + max(numbers[i:i + c])


print(get_solution(numbers, get_invalid_number(numbers)))
