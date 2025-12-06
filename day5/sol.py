def _in_range(range: tuple[int, int], id: int):
    return id >= range[0] and id <= range[1]


def part_one(ranges: list[tuple[int, int]], ids: list[int]) -> int:

    fresh = 0

    for id in ids:
        fresh += 1 if any(_in_range(rang, id) for rang in ranges) else 0

    return fresh


def part_two(ranges: list[tuple[int, int]]) -> int:

    fresh = 0

    # Merge overlapping and adjacent ranges to avoid redundant counting
    merged = []
    for start, end in sorted(ranges):
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    fresh = sum(end - start + 1 for start, end in merged)

    return fresh


if __name__ == "__main__":

    ranges = []
    ids = []

    with open("input.txt", "+r") as f:
        id = False
        for line in f:

            if line == "\n":
                id = True
                continue

            if not id:
                l, r = line.strip().split("-")
                ranges.append((int(l), int(r)))
            else:
                ids.append(int(line.strip()))

    p1_fresh = part_one(ranges, ids)

    print("The total rolls for part one is", p1_fresh)

    p2_fresh = part_two(ranges)

    print("The total rolls for part two is", p2_fresh)
