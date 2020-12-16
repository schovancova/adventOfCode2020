ASSIGNMENT = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def traverse(lines, right, down):
    trees = 0
    pos = 0
    for line in lines[::down]:
        if pos > len(line) - 1:
            pos -= len(line)
        if line[pos] == "#":
            trees += 1
        pos += right
    return trees


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        res = 1
        for right, down in ASSIGNMENT:
            res *= traverse(lines, right, down)
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
