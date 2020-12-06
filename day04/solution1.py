import re

with open("input.txt", "r") as f:
    passports = f.read().split("\n\n")

needed_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
num_valid = 0
for passport in passports:
    passport = re.split("\n| ", passport.strip())
    passport = {r[0]: r[1] for s in passport if (r := s.split(":"))}
    if all(k in passport for k in needed_keys):
        num_valid += 1
print(num_valid)
