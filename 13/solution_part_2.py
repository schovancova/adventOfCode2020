from sympy.ntheory.modular import crt


def main():
    with open('input.txt') as f:
        f.readline()
        buses = f.readline().split(",")
        n = []
        a = []
        for ix, bus in enumerate(buses):
            if bus != "x":
                n.append(int(bus))
                a.append(int(bus) - ix)
        res = crt(n, a)
        print(f"Result is {res[0]}")


if __name__ == "__main__":
    main()


