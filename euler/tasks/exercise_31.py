COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def count_ways(target, coins=COINS):
    if target < 0:
        raise ValueError("target must be >= 0")
    if any(coin < 1 for coin in coins):
        raise ValueError("every coin must be >= 1")

    ways = [1] + [0] * target
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    return ways[target]
