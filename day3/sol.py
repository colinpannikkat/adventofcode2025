# from functools import cache


def part_one(banks: list[str]) -> int:

    joltage = 0

    for bank in banks:  # O(m)

        bank_arr = [int(b) for b in bank]

        # O(n^2)
        # max_jolt = 0
        # for i in range(len(bank_arr)):
        #     for j in range(i+1, len(bank_arr)):
        #         max_jolt = max(max_jolt, int(str(bank_arr[i]) + str(bank_arr[j])))
        # joltage += max_jolt

        # O(n)
        first_max = max(bank_arr[:len(bank_arr)-1])
        first_max_idx = bank_arr.index(first_max)
        second_max = max(bank_arr[first_max_idx+1:])
        joltage += int(str(bank_arr[first_max_idx]) + str(second_max))

    return joltage


def part_two(banks: list[str]) -> int:

    joltage = 0

    for bank in banks:  # O(m)

        # DP solution, too slow
        # @cache
        # def dp(b, sequence):

        #     if len(sequence) == 12 or len(b) == 0:  # at the end or hit limit of 12
        #         return int(sequence) if sequence != '' else 0

        #     # Pick
        #     pick = dp(b[1:], sequence + str(b[0]))

        #     # Don't pick
        #     dont = dp(b[1:], sequence)

        #     return max(pick, dont)

        # joltage += dp(bank, "")

        # Decreasing monotonic stack, O(n)
        s = []
        remove = len(bank) - 12  # deletions allowed
        for b in bank:
            while s != [] and remove > 0 and s[-1] < b:
                s.pop()
                remove -= 1
            s.append(b)

        while remove > 0:
            s.pop()
            remove -= 1

        joltage += int(''.join(s))

    return joltage


if __name__ == "__main__":

    with open("input.txt", "+r") as f:
        input = [line.strip() for line in f]

    p1_joltage = part_one(input)

    print("The total output joltage for part one is", p1_joltage)

    p2_joltage = part_two(input)

    print("The total output joltage for part two is", p2_joltage)
