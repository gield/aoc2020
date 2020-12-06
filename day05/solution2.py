with open("input.txt", "r") as f:
    boarding_passes = [s.strip() for s in f.readlines()]

seat_ids = []
for boarding_pass in boarding_passes:
    row_number = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col_number = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    seat_ids.append(row_number * 8 + col_number)

for seat in range(min(seat_ids), max(seat_ids) + 1):
    if seat not in seat_ids and seat + 1 in seat_ids and seat - 1 in seat_ids:
        print(seat)
