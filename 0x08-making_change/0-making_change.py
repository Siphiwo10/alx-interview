#!/usr/bin/python3
"""Make chang main filee"""


def makeChange(coins: list, total):
    """make change function
    takes coin, total
    return:
    """
    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
