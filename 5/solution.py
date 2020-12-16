def get_bound(half, bottom, top, lower, upper):
    if half == bottom:
        upper = ((lower + upper + 1) // 2) - 1
    elif half == top:
        lower = ((lower + upper + 1) // 2)
    return lower, upper


def parse_row(line):
    lower = 0
    upper = 127
    for half in line:
        lower, upper = get_bound(half, "F", "B", lower, upper)
    return lower


def parse_column(line):
    lower = 0
    upper = 7
    for half in line:
        lower, upper = get_bound(half, "L", "R", lower, upper)
    return lower


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        res = []
        for line in lines:
            row = parse_row(line[:7])
            col = parse_column(line[7:])
            seat_id = row * 8 + col
            res.append(seat_id)
    print(f"PART1: Result is {max(res)}")
    print(f"PART2: Result is {find_missing(sorted(res))}")


if __name__ == "__main__":
    main()
