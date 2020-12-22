import math


def rotate_waypoint(w_x, w_y, angle):
    # rotate against (0,0)
    x = w_x * round(math.cos(math.radians(angle))) + w_y * round(math.sin(math.radians(angle)))
    y = - w_x * round(math.sin(math.radians(angle))) + w_y * round(math.cos(math.radians(angle)))
    return x, y


def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()
        # waypoint offset
        w_x = 10
        w_y = 1
        # boat
        x = y = 0
        for line in lines:
            instr, num = line[:1], int(line[1:])
            if instr == "N":
                w_y += num
            elif instr == "S":
                w_y -= num
            elif instr == "E":
                w_x += num
            elif instr == "W":
                w_x -= num
            elif instr == "R":
                w_x, w_y = rotate_waypoint(w_x, w_y, num)
            elif instr == "L":
                w_x, w_y = rotate_waypoint(w_x, w_y, -num)
            elif instr == "F":
                x += w_x * num
                y += w_y * num
            print(f"Waypoint x {w_x} {w_y}, Boat {x} {y}, Instruction {line}")
    print(f"Result is {abs(x)+abs(y)}")


if __name__ == "__main__":
    main()
