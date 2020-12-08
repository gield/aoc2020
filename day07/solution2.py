import re

with open("input.txt", "r") as f:
    raw_rules = [r.strip() for r in f.readlines()]

rules = {}
for r in raw_rules:
    key, raw_values = re.compile("([a-z ]*) bags contain (.*)").findall(r)[0]
    parsed_values = re.compile("(\d) ([a-z ]*) bag").findall(raw_values)
    values = {color: int(num) for num, color in parsed_values}
    rules[key] = values

def get_num_bags(target_color):
    rule = rules[target_color]
    if not rule.values():
        return 1
    return 1 + sum(get_num_bags(color) * num for color, num in rule.items())
print(get_num_bags("shiny gold") - 1)
