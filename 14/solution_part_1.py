
def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        res = dict()
        for line in lines:
            if "mask" in line:
                mask = list(line.split("=")[1].strip())
            else:
                pos, num = ''.join(c for c in line if c.isdigit() or c == " ").split()
                binary = list(f"{int(num):b}".zfill(len(mask)))
                for idx, val in enumerate(mask):
                    if val != "X":
                        binary[idx] = val
                res[pos] = int(''.join(binary), 2)
    print(f"Result is {sum(res.values())}")


if __name__ == "__main__":
    main()
