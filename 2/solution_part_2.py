def main():
    with open('input.txt') as f:
        records = f.read().splitlines()
        res = 0
        for record in records:
            first, second, char, pw = record.replace('-', ' ').replace(': ', ' ').split()
            if (pw[int(first)-1] == char) != (pw[int(second)-1] == char):
                res += 1
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
