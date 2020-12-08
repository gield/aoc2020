import re

with open("input.txt", "r") as f:
    raw_rules = [r.strip() for r in f.readlines()]

rules = {}
for r in raw_rules:
    key, raw_values = re.compile("([a-z ]*) bags contain (.*)").findall(r)[0]
    parsed_values = re.compile("(\d) ([a-z ]*) bag").findall(raw_values)
    values = {color: int(num) for num, color in parsed_values}
    rules[key] = values

colors_to_find = {"shiny gold"}
suitable_colors = set()
while colors_to_find:
    new_colors = set()
    for color, contents in rules.items():
        if any(c in contents.keys() for c in colors_to_find):
            new_colors.add(color)
    colors_to_find = new_colors
    suitable_colors |= new_colors
print(len(suitable_colors))
