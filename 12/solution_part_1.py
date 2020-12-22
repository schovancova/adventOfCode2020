def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        x = y = 0
        rot = 90
        for line in lines:
            instr, num = line[:1], int(line[1:])
            if instr == "N" or (instr == "F" and rot == 0):
                y += num
            elif instr == "S" or (instr == "F" and abs(rot) == 180):
                y -= num
            elif instr == "E" or (instr == "F" and rot in [90, -270]):
                x += num
            elif instr == "W" or (instr == "F" and rot in [270, -90]):
                x -= num
            elif instr == "R":
                rot += num
                rot -= 360 if rot >= 360 else 0
            elif instr == "L":
                rot -= num
                rot += 360 if rot <= -360 else 0

    print(f"Result is {abs(x)+abs(y)}")


if __name__ == "__main__":
    main()