from copy import deepcopy


def adjacent_cells(grid, y, x):
    neighbours = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
    return list(
        grid[b][a] if 0 <= b < len(grid) and 0 <= a < len(grid[b])
        else None
        for (a, b) in neighbours)


def calculate_new_grid(grid):
    new_grid = deepcopy(grid)
    for idx, row in enumerate(grid):
        for idx2, col in enumerate(row):
            adjacent = adjacent_cells(grid, idx, idx2)
            if grid[idx][idx2] == "L" and "#" not in adjacent:
                new_grid[idx][idx2] = "#"
            elif grid[idx][idx2] == "#" and adjacent.count("#") > 3:
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
