
def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        group = set()
        res = 0
        for line in lines:
            if line:
                line = list(line)
                group.update(line)
            else:
                res += len(group)
                group = set()
        res += len(group)
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
