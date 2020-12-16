def is_sum_in_preamble(pre, num):
    for p in pre:
        if (num - p) in pre:
            return True
    return False


def find_weak_list(weakness):
    with open('input.txt') as f:
        lines = f.read().splitlines()
        nums = []
        for line in lines:
            line = int(line)
            nums.append(line)
            if sum(nums) == weakness:
                return nums
            elif sum(nums) > weakness:
                while sum(nums) > weakness:
                    nums.pop(0)
                if sum(nums) == weakness: return nums


def get_weakness():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        pre_length = 25
        preamble = []
        for line in lines:
            if pre_length != len(preamble):
                preamble.append(int(line))
            else:
                is_sum = is_sum_in_preamble(preamble, int(line))
                if is_sum:
                    preamble = preamble[1:]
                    preamble.append(int(line))
                else:
                    return int(line)


def main():
    weakness = get_weakness()
    contiguous = find_weak_list(weakness)
    res = min(contiguous) + max(contiguous)
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
