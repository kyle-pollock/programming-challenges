import sys

MAX_STICK_LENGTH = 1000
memo = {}


def minimum_cutting_cost(L, R, cut_positions):
    if (L, R) in memo:
        return memo[(L, R)]
    if not cut_positions:
        memo[(L, R)] = 0
        return 0

    minimum_cost = sys.maxsize
    for i, cut_position in enumerate(cut_positions):
        cost = (R - L) + minimum_cutting_cost(
            L, cut_position, cut_positions[:i]) + minimum_cutting_cost(
                cut_position, R, cut_positions[i + 1:])

        if cost < minimum_cost:
            minimum_cost = cost

    memo[(L, R)] = minimum_cost
    return minimum_cost


for line in sys.stdin:
    stick_length = int(line)
    if stick_length == 0:
        break
    num_cuts = int(sys.stdin.readline())
    cut_positions = [int(x) for x in sys.stdin.readline().split()]

    memo = {}
    print(
        f'The minimum cutting is {minimum_cutting_cost(0, stick_length, cut_positions)}.'
    )
