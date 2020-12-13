with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

timestamp = int(lines[0])
buses = [int(b) for b in lines[1].split(",") if b != "x"]

for t in range(timestamp, timestamp + max(buses)):
    for b in buses:
        if t % b == 0:
            print(b * (t - timestamp))
            exit(0)
