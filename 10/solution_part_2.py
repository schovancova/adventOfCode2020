
def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        lines = sorted(list(map(int, lines)))
        lines.append(lines[-1] + 3)
        res = {0: 1}
        for a in lines:
            res[a] = res.get(a-1, 0) + res.get(a-2, 0) + res.get(a-3, 0)
        print(f'Result is {res[lines[-1]]}')


if __name__ == "__main__":
    main()
