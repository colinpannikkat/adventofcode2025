def part_one(codes: list[str]) -> int:

    zero = 0  # number of times dial hits zero
    dial = 50  # starts pointing at 50

    for code in codes:

        dir, num = code[0], int(code[1:])

        delta = dial - num if dir == "L" else dial + num

        dial = delta % 100

        if dial == 0:
            zero += 1

    return zero


def part_two(codes: list[str]) -> int:

    zero = 0  # number of times click hits zero
    dial = 50  # starts point at 50

    for code in codes:

        dir, num = code[0], int(code[1:])

        delta = dial - num if dir == "L" else dial + num

        if (dial > 0 and delta <= 0) or delta == 0:  # case where it goes pos to neg (or 0)
            zero += 1
        zero += abs(int(delta / 100))  # count crossings

        dial = delta % 100

    return zero


if __name__ == "__main__":

    with open("input.txt", "+r") as f:
        codes = f.readlines()

    p1_password = part_one(codes)

    print("The password for part one is", p1_password)

    p2_password = part_two(codes)

    print("The password for part two is", p2_password)
