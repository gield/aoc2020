import itertools

with open("input.txt", "r") as f:
    card_key, door_key = [int(l) for l in f.read().strip().split("\n")]

subject_number = 7
value = 1
for loop_size in itertools.count(1):
    _, value = divmod(value * subject_number, 20201227)
    if value == card_key:
        subject_number = door_key
        break
    if value == door_key:
        subject_number = card_key
        break

value = 1
for _ in range(loop_size):
    _, value = divmod(value * subject_number, 20201227)
print(value)
