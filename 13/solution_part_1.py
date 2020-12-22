import math


def main():
    with open('input.txt') as f:
        time = res = int(f.readline())
        buses = f.readline().split(",")
        buses = [int(x) for x in buses if x != 'x']
        for bus in buses:
            wait_time = (math.ceil(time/bus) * bus) - time
            if wait_time < res:
                res = wait_time
                res_bus = bus
    print(f"Result is {res*res_bus}")


if __name__ == "__main__":
    main()
