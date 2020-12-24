
def main():
    rules = {}
    with open('input.txt') as f:
        line = f.readline()
        while line != "\n":
            name, ranges = line.split(": ")
            first, second = ranges.split(" or ")
            first = first.split("-")
            second = second.split("-")
            rules[name] = [[int(first[0]), int(first[1])], [int(second[0]), int(second[1])]]
            line = f.readline()
        f.readline();f.readline();f.readline();f.readline()
        lines = f.read().splitlines()
        res = 0
        for line in lines:
            line = line.split(",")
            for num in line:
                num = int(num)
                valid = False
                for first, second in list(rules.values()):
                    if first[0] <= num <= first[1] or second[0] <= num <= second[1]:
                        valid = True
                        break
                if not valid:
                    res += num
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
