import re


def validate_batch(batch_file):
    batch = batch_file.split("\n\n")
    valid_count = 0
    for passport_string in batch:
        passport = parse_passport(passport_string)
        if validate_passport(passport):
            valid_count += 1
    return valid_count


def parse_passport(passport_string):
    raw_fields = passport_string.replace("\n", " ").split(" ")
    passport = {}
    for field in raw_fields:
        pair = field.split(":", maxsplit=1)
        if pair[0] != '':
            passport[pair[0]] = pair[1]
    return passport


def validate_passport(passport):
    for key, validator in key_validators.items():
        try:
            if not validator(passport[key]):
                return False
        except:
            return False
    return True


key_validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
    'hcl': lambda x: re.match(r"^#[0-9a-f]{6}$", x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: int(x) and len(x) == 9
}

with open("input.txt") as fp:
    print(validate_batch(fp.read()))
