import re
import string

with open("input.txt", "r") as f:
    passports = f.read().split("\n\n")

def is_valid_number(s, low, high):
    return s.isnumeric() and low <= int(s) <= high
    

def is_valid_passport(pp):
    if not all(k in pp for k in needed_keys):
        return False

    if not is_valid_number(pp["byr"], 1920, 2002):
        return False
    if not is_valid_number(pp["iyr"], 2010, 2020):
        return False
    if not is_valid_number(pp["eyr"], 2020, 2030):
        return False
    
    if pp["hgt"].endswith("cm"):
        if not is_valid_number(pp["hgt"][:-2], 150, 193):
            return False
    elif pp["hgt"].endswith("in"):
        if not is_valid_number(pp["hgt"][:-2], 59, 76):
            return False
    else:
        return False
    
    if pp["hcl"][0] != "#" or len(pp["hcl"]) != 7:
        return False
    if not all(c in string.hexdigits for c in pp["hcl"][1:]):
        return False
    
    if not pp["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    
    if not (pp["pid"].isnumeric() and len(pp["pid"]) == 9):
        return False
    
    return True
    
    
    

needed_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
num_valid = 0
for passport in passports:
    passport = re.split("\n| ", passport.strip())
    passport = {r[0]: r[1] for s in passport if (r := s.split(":"))}
    if is_valid_passport(passport):
        num_valid += 1
print(num_valid)
