from copy import deepcopy


def adjacent_cells(grid, y, x):
    neighbours = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    res = []
    for (a, b) in neighbours:
        real_y = y+b
        real_x = x+a
        if 0 <= real_y < len(grid) and 0 <= real_x < len(grid[real_y]):
            while grid[real_y][real_x] not in ["#", "L"]:
                if 0 <= real_y+b < len(grid) and 0 <= real_x+a < len(grid[real_y+b]):
                    real_y += b
                    real_x += a
                else:
                    # we hit a wall
                    break
            if grid[real_y][real_x] in ["#", "L"]:
                res.append(grid[real_y][real_x])
    return res


def calculate_new_grid(grid):
    new_grid = deepcopy(grid)
    for idx, row in enumerate(grid):
        for idx2, col in enumerate(row):
            adjacent = adjacent_cells(grid, idx, idx2)
            if grid[idx][idx2] == "L" and "#" not in adjacent:
                new_grid[idx][idx2] = "#"
            elif grid[idx][idx2] == "#" and adjacent.count("#") >= 5:
                new_grid[idx][idx2] = "L"
    return new_grid


def main():
    grid = []
    with open('input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            grid.append(list(line))
    new_grid = calculate_new_grid(grid)
    while new_grid != grid:
        grid = new_grid
        new_grid = calculate_new_grid(grid)
    res = 0
    for row in new_grid:
        res += row.count("#")
    print(f"Result is {res}")


if __name__ == "__main__":
    main()
