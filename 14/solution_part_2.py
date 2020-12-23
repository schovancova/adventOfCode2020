import itertools


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        res = dict()
        for line in lines:
            if "mask" in line:
                mask = list(line.split("=")[1].strip())
            else:
                pos, num = ''.join(c for c in line if c.isdigit() or c == " ").split()
                binary = list(f"{int(pos):b}".zfill(len(mask)))
                for idx, val in enumerate(mask):
                    if val != "0":
                        binary[idx] = val
                exes = binary.count("X")
                perms = [p for p in itertools.product([0, 1], repeat=binary.count("X"))]
                for perm in perms:
                    new_bin = binary.copy()
                    p_id = 0
                    for idx, c in enumerate(new_bin):
                        if c == "X":
                            new_bin[idx] = str(perm[p_id])
                            p_id += 1
                    addr = int(''.join(new_bin), 2)
                    res[addr] = int(num)
    print(f"Result is {sum(res.values())}")


if __name__ == "__main__":
    main()
