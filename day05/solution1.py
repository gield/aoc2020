with open("input.txt", "r") as f:
    boarding_passes = [s.strip() for s in f.readlines()]

highest_seat_id = 0
for boarding_pass in boarding_passes:
    row_number = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col_number = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    if (seat_id := row_number * 8 + col_number) > highest_seat_id:
        highest_seat_id = seat_id
print(highest_seat_id)
