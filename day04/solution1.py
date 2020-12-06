import re

with open("input.txt", "r") as f:
    passports = [p.strip() for p in f.read().split("\n\n")]

needed_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
num_valid = 0
for passport in passports:
    split_passport = re.split("\n| ", passport)
    fields = {r[0]: r[1] for s in split_passport if (r := s.split(":"))}
    if all(k in fields for k in needed_keys):
        num_valid += 1
print(num_valid)
