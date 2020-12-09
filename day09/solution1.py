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


print(get_invalid_number(numbers))
