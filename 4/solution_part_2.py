import re
REQ = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate(passport):
    if not (passport["byr"].isdigit() and 1920 <= int(passport["byr"]) <= 2020):
        return False
    if not (passport["iyr"].isdigit() and 2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not (passport["eyr"].isdigit() and 2020 <= int(passport["eyr"]) <= 2030):
        return False

    if "cm" in passport["hgt"]:
        height = passport["hgt"][:-2]
        if not (height.isdigit() and 150 <= int(height) <= 193):
            return False
    elif "in" in passport["hgt"]:
        height = passport["hgt"][:-2]
        if not (height.isdigit() and 59 <= int(height) <= 76):
            return False
    else:
        return False
    pattern = re.compile("^#([a-f]|[0-9]){6}$")
    if not pattern.match(passport["hcl"]):
        return False
    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not (passport["pid"].isdigit() and len(passport["pid"]) == 9):
        return False
    return True


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        valid = 0
        missing = len(REQ)
        passport = {}
        for line in lines:
            if not line:
                valid += 1 if not missing and validate(passport) else 0
                missing = len(REQ)
            else:
                line = line.split(" ")
                for item in line:
                    key, value = item.split(":")
                    if key in REQ:
                        passport[key] = value
                        missing -= 1
        valid += 1 if not missing and validate(passport) else 0
    print(f"Result is {valid}")


if __name__ == "__main__":
    main()
