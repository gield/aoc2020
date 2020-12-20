with open("input.txt", "r") as f:
    fields_raw, _, nearby_tickets_raw = [l.strip().split("\n") for l in f.read().split("\n\n")]

fields = {}
for field_raw in fields_raw:
    name, remainder = field_raw.split(": ")
    range1, range2 = [[int(i) for i in r.split("-")] for r in remainder.split(" or ")]
    fields[name] = {*range(range1[0], range1[1] + 1), *range(range2[0], range2[1] + 1)}

nearby_tickets = [[int(i) for i in l.split(",")] for l in nearby_tickets_raw[1:]]

solution = 0
for ticket in nearby_tickets:
    for ticket_field in ticket:
        if not any(ticket_field in field_range for field_range in fields.values()):
            solution += ticket_field
print(solution)
