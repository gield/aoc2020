with open("input.txt", "r") as f:
    cups = [int(c) for c in f.read().strip()]

num_cups = len(cups)
current_cup_i = 0
for move in range(100):
    current_cup = cups[current_cup_i]

    pick_up = [cups[(current_cup_i + 1 + i) % num_cups] for i in range(3)]
    cups = [c for c in cups if c not in pick_up]

    for i in range(num_cups - 4):
        # Lower destination value by 1 each time
        # Note: `or num_cups` makes sure we go from 1 to 9 instead of 1 to 0
        destination_value = (current_cup - i - 1) % num_cups or num_cups
        if destination_value in cups:
            break

    destination_i = cups.index(destination_value)
    cups = cups[:destination_i + 1] + pick_up + cups[destination_i + 1:]
    current_cup_i = (cups.index(current_cup) + 1) % num_cups

index_of_1 = cups.index(1)
solution_cups = cups[index_of_1 + 1:] + cups[:index_of_1]
print("".join(str(i) for i in solution_cups))
