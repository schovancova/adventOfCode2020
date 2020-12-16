def main():
    with open('input.txt') as f:
        records = f.read().splitlines()
        res = 0
        for record in records:
            min_v, max_v, char, pw = record.replace('-', ' ').replace(': ', ' ').split()
            if int(min_v) <= pw.count(char) <= int(max_v):
                res += 1
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
