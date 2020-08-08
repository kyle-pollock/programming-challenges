import sys

MAX_STICK_LENGTH = 1000


def minimum_cutting_cost(L, R, cut_positions, memo):
    if (L, R) in memo:
        return memo[(L, R)]
    if len(cut_positions) == 0:
        memo[(L, R)] = 0
        return 0

    minimum_cost = MAX_STICK_LENGTH + 1
    for i, cut_position in enumerate(cut_positions):
        cost = (R - L) + minimum_cutting_cost(
            L, cut_position, cut_positions[:i], memo) + minimum_cutting_cost(
                cut_position, R, cut_positions[i + 1:], memo)

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

    print(
        f'The minimum cutting is {minimum_cutting_cost(0, stick_length, cut_positions, {})}.'
    )
