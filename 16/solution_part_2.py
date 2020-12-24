# todo
def is_valid(rules, nums):
    for num in nums:
        valid = False
        for first, second in list(rules.values()):
            if first[0] <= num <= first[1] or second[0] <= num <= second[1]:
                valid = True
        if not valid:
            return False
    return True


def main():
    rules = {}
    with open('input.txt') as f:
        line = f.readline()
        # parse rules
        while line != "\n":
            name, ranges = line.split(": ")
            first, second = ranges.split(" or ")
            first = first.split("-")
            second = second.split("-")
            rules[name] = [[int(first[0]), int(first[1])], [int(second[0]), int(second[1])]]
            line = f.readline()
        # parse my ticket
        f.readline()
        line = f.readline()
        my_ticket = [int(a) for a in line.split(",")]
        f.readline();f.readline()

        #parse other's tickets
        valid_tickets = []
        for line in f.read().splitlines():
            line = [int(a) for a in line.split(",")]
            if is_valid(rules, line):
                valid_tickets.append(line)
        print(rules)
        print(my_ticket)
        print(valid_tickets)

        for field in range(0, len(my_ticket)):
            samples = [x[0] for x in valid_tickets]
            for name, ranges in rules.items():
                pass


    print(f"Result is {0}")


if __name__ == "__main__":
    main()
