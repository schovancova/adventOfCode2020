from collections import defaultdict


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        group = defaultdict(int)
        people = 0
        res = 0
        for line in lines:
            if line:
                for l in line:
                    group[l] += 1
                people += 1
            else:
                res += list(group.values()).count(people)
                people = 0
                group = defaultdict(int)
        res += list(group.values()).count(people)
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
