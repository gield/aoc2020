from typing import Dict, List, Union
import re

with open("input.txt", "r") as f:
    raw_rules, messages = [l.strip().split("\n") for l in f.read().split("\n\n")]

rules: Dict[int, Union[str, List[List[int]]]] = {}
for raw_rule in raw_rules:
    i, r = raw_rule.split(": ")
    if r[0] == "\"":
        rules[int(i)] = r[1:-1]
    else:
        rules[int(i)] = [[int(j) for j in s.split()] for s in r.split(" | ")]


rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]


def create_regex(rule_i):
    rule = rules[rule_i]
    if type(rule) == str:
        return rule
    elif rule_i == 8:
        return create_regex(42) + "+"
    elif rule_i == 11:
        rule_42 = create_regex(42)
        rule_31 = create_regex(31)
        regex = []
        for i in range(1, 100):
            regex.append(rule_42 + "{" + str(i) + "}" + rule_31 + "{" + str(i) + "}")
        return "(?:" + "|".join(regex) + ")"
    else:
        regex = "|".join("".join(create_regex(i) for i in subrule) for subrule in rule)
        return "(?:" + regex + ")"


pattern = "^" + create_regex(0) + "$"
print(sum(1 if re.match(pattern, message) else 0 for message in messages))
