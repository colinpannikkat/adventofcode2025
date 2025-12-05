def part_one(grid: list[list[str]]) -> tuple[int, list[list[str]]]:

    rolls = 0
    m, n = len(grid), len(grid[0])

    out_grid = [row[:] for row in grid]  # copy for output

    for j in range(m):
        for i in range(n):

            if grid[j][i] != '@':
                continue

            count = 0

            # Check up
            if j > 0:
                if grid[j-1][i] == '@':
                    count += 1

            # Check down
            if j < m - 1:
                if grid[j+1][i] == '@':
                    count += 1

            # Check left
            if i > 0:
                if grid[j][i - 1] == '@':
                    count += 1

            # Check right
            if i < n - 1:
                if grid[j][i + 1] == '@':
                    count += 1

            # Check up/left
            if j > 0 and i > 0:
                if grid[j - 1][i - 1] == '@':
                    count += 1

            # Check up/right
            if j > 0 and i < n - 1:
                if grid[j - 1][i + 1] == '@':
                    count += 1

            # Check down/left
            if j < m - 1 and i > 0:
                if grid[j + 1][i - 1] == '@':
                    count += 1

            # Check down/right
            if j < m - 1 and i < n - 1:
                if grid[j + 1][i + 1] == '@':
                    count += 1

            if count < 4:
                rolls += 1
                out_grid[j][i] = 'x'

    return rolls, out_grid


def part_two(grid: list[list[str]]) -> int:

    rolls = 0

    while True:
        count, grid = part_one(grid)

        if count == 0:
            break

        rolls += count

    return rolls


if __name__ == "__main__":

    with open("input.txt", "+r") as f:
        input = [list(line.strip()) for line in f]

    p1_rolls = part_one(input)[0]

    print("The total rolls for part one is", p1_rolls)

    p2_rolls = part_two(input)

    print("The total rolls for part two is", p2_rolls)
