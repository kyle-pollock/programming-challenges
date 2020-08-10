import sys

coin_types = [ 50, 25, 10, 5, 1]
memo = {}

def ways_to_make_change(amount):
    return ways_to_make_change_recursive(amount, 0)

def ways_to_make_change_recursive(amount, coin_index):
    key = (amount, tuple(coin_types[coin_index:]))
    if key in memo:
        return memo[key]
    if amount == 0:
        memo[key] = 1
        return 1
    if coin_index == len(coin_types):
        memo[key] = 0
        return 0

    ways = 0
    amountWithCoin = 0
    while amountWithCoin <= amount:
        remaining = amount - amountWithCoin
        ways += ways_to_make_change_recursive(remaining , coin_index + 1)
        amountWithCoin += coin_types[coin_index]

    memo[key] = ways
    return ways


for line in sys.stdin:
    amount = int(line)
    print(ways_to_make_change(amount))
