from typing import Dict

with open("input.txt", "r") as f:
    fields_raw, your_ticket_raw, nearby_tickets_raw = [l.strip().split("\n") for l in f.read().split("\n\n")]

fields = {}
for field_raw in fields_raw:
    name, remainder = field_raw.split(": ")
    range1, range2 = [[int(i) for i in r.split("-")] for r in remainder.split(" or ")]
    fields[name] = {*range(range1[0], range1[1] + 1), *range(range2[0], range2[1] + 1)}

your_ticket = [int(i) for i in your_ticket_raw[1].split(",")]
nearby_tickets = [[int(i) for i in l.split(",")] for l in nearby_tickets_raw[1:]]

valid_tickets = []
for ticket in nearby_tickets:
    for ticket_field in ticket:
        if not any(ticket_field in field_range for field_range in fields.values()):
            break
    else:
        valid_tickets.append(ticket)

field_placement = {field_i: set(fields.keys()) for field_i in range(len(your_ticket))}
for ticket in valid_tickets:
    for i, ticket_field in enumerate(ticket):
        currently_possible_fields = field_placement[i]
        to_remove = {name for name in currently_possible_fields if ticket_field not in fields[name]}
        field_placement[i] -= to_remove

final_field_placement: Dict[int, str] = {}
for i, field_names in sorted(field_placement.items(), key=lambda t: len(t[1])):
    field_names -= set(final_field_placement.values())
    if len(field_names) == 1:
        final_field_placement[i] = next(iter(field_names))

solution = 1
for i, field_name in final_field_placement.items():
    if field_name.startswith("departure"):
        solution *= your_ticket[i]
print(solution)
