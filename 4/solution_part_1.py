REQ = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        valid = 0
        missing = len(REQ)
        for line in lines:
            if not line:
                valid += 1 if not missing else 0
                missing = len(REQ)
            else:
                line = line.split(" ")
                for item in line:
                    if item.split(":")[0] in REQ:
                        missing -= 1
        valid += 1 if not missing else 0
    print(f"Result is {valid}")


if __name__ == "__main__":
    main()
