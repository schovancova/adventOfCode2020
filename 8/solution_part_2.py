def is_infinite(formatted, idx_to_swap):
    idx = acc = 0
    visited = []
    while True:
        code, num = formatted[idx]
        if idx == idx_to_swap:
            code = "jmp" if code == "nop" else "nop"
        if idx in visited:
            return None
        visited.append(idx)
        if code == "acc":
            acc += int(num)
            idx += 1
        elif code == "jmp":
            idx += int(num)
        else:
            idx += 1
        if idx >= len(formatted):
            return acc


def main():
    exc_idxs = []
    with open('input.txt') as f:
        lines = f.read().splitlines()
        formatted = []
        for idx, line in enumerate(lines):
            code, num = line.split(" ")
            if code in ["jmp", "nop"]:
                exc_idxs.append(idx)
            formatted.append([code, int(num)])
    for exc_idx in exc_idxs:
        res = is_infinite(formatted, exc_idx)
        if res is not None:
            print(f"Result is {res}")


if __name__ == "__main__":
    main()
