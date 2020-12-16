def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        trees = 0
        pos = 0
        for line in lines:
            if pos > len(line)-1:
                pos -= len(line)
            if line[pos] == "#":
                trees += 1
            pos += 3
    print(f"Result is {trees}")


if __name__ == "__main__":
    main()
