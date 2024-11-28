#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to achieve.
    
    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins are needed for a total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
