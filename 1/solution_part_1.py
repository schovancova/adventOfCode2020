SUM_ASSIGNED = 2020


def main():
    with open('input.txt') as f:
        raw_nums = f.read().splitlines()
        nums = list(map(int, raw_nums))
        for first_idx, first_num in enumerate(nums):
            for second_idx, second_num in enumerate(nums):
                # do not compare same index numbers
                if first_idx == second_idx:
                    continue
                if first_num + second_num == SUM_ASSIGNED:
                    print(f"Result is {first_num * second_num}")
                    return


if __name__ == "__main__":
    main()
