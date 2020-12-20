from collections import defaultdict

with open("input.txt", "r") as f:
    starting_numbers = [int(n) for n in f.readline().split(",")]

numbers_dict = defaultdict(lambda: [])
turn = 1
for n in starting_numbers:
    numbers_dict[n].append(turn)
    turn += 1

final_turn = 2020
last_number = starting_numbers[-1]
while turn <= final_turn:
    if len(numbers_dict[last_number]) == 1:
        last_number = 0
    else:
        history = numbers_dict[last_number]
        last_number = history[-1] - history[-2]
    numbers_dict[last_number].append(turn)
    if turn == final_turn:
        print(last_number)
    turn += 1
