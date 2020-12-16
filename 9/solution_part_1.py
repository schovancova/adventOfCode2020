def is_sum_in_preamble(pre, num):
    for p in pre:
        if (num - p) in pre:
            return True
    return False


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        pre_length = 25
        preamble = []
        res = 0
        for line in lines:
            if pre_length != len(preamble):
                preamble.append(int(line))
            else:
                is_sum = is_sum_in_preamble(preamble, int(line))
                if is_sum:
                    preamble = preamble[1:]
                    preamble.append(int(line))
                else:
                    res = int(line)
                    break
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
