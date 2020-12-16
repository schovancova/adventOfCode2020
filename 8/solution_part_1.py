
def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        acc = idx = 0
        visited = []
        while True:
            if idx in visited:
                print(f"Result is {acc}")
                return acc
            visited.append(idx)
            instr = lines[idx]
            code, num = instr.split(" ")
            if code == "acc":
                acc += int(num)
                idx += 1
            elif code == "jmp":
                idx += int(num)
            else:
                idx += 1


if __name__ == "__main__":
    main()
