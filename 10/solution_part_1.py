
def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        lines = sorted(list(map(int, lines)))
        lines.insert(0, 0)
        lines.append(lines[-1] + 3)
        diffs = [j-i for i, j in zip(lines[:-1], lines[1:])]
        res = diffs.count(1) * diffs.count(3)
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
