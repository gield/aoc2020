import itertools

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

buses = [int(b) if b != "x" else "x" for b in lines[1].split(",")]
enumerated_buses = [(i, b) for i, b in enumerate(buses) if b != "x"]


def generate_common_timestamps(start_t, enumerated_buses, step):
    for t in itertools.count(start_t, step):
        for i, b in enumerated_buses:
            if (t + i) % b != 0:
                break
            if b == enumerated_buses[-1][1]:
                yield t


start_t = 0
step = enumerated_buses[0][1]
for n in range(len(enumerated_buses)):
    generator = generate_common_timestamps(start_t, enumerated_buses[:n + 1], step)
    t, next_t = next(generator), next(generator)
    start_t = t
    step = next_t - t
print(t)
