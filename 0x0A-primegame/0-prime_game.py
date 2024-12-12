#!/usr/bin/python3
"""isWinner """


def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): Array of integers, where nums[i] represents n for round i
    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None
    """
    if not nums or x < 1:
        return None

    # Precompute primes up to the maximum value in nums using Siev
    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of odd, Maria wins; otherwise, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
