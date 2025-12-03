# This shit is so brute force lol

def part_one(ids: list[tuple[str, str]]) -> int:

    count = 0

    for (left, right) in ids:

        for id in range(int(left), int(right) + 1):

            id = str(id)

            if id[0] == "0":
                count += int(id)
            # split into half
            elif len(id) % 2 == 0:

                first, second = id[:(len(id)//2)], id[(len(id)//2):]

                if first == second:
                    count += int(id)

    return count


def part_two(ids: list[tuple[str, str]]) -> int:

    count = 0

    for (left, right) in ids:

        for id in range(int(left), int(right) + 1):

            id = str(id)

            for k in range(2, len(id) + 1):  # split into 2 until len(id)

                if len(id) % k == 0:  # can evenly split

                    splits = []

                    for j in range(k):  # get all sub dividing splits
                        splits.append(id[(j * len(id) // k):((j + 1) * len(id) // k)])

                    if all(map(lambda x: x == splits[0], splits)):
                        count += int(id)
                        break

    return count


if __name__ == "__main__":

    ids = []

    with open("input.txt", "+r") as f:
        input = f.read().strip()

        for rang in input.split(","):
            l, r = rang.split("-")
            ids.append((l, r))

    p1_invalid = part_one(ids)

    print("The invalid IDs for part one is", p1_invalid)

    p2_invalid = part_two(ids)

    print("The invalid IDs for part two is", p2_invalid)
