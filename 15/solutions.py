from collections import defaultdict


def main():
    with open('input.txt') as f:
        nums = list(map(int, f.readline().split(",")))
        for part, count_to in enumerate((2020, 30000000)):
            last_seen = defaultdict(lambda: i, {n: i for i, n in enumerate(nums[:-1])})
            prev = nums[-1]
            for i in range(len(nums) - 1, count_to - 1):
                last_seen[prev], prev = i, i - last_seen[prev]
            print(f'Result part {part+1}: {prev}')


if __name__ == "__main__":
    main()
