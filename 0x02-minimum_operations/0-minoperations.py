#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    """main function"""
    if n < 2:
        return 0

    result = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            result += divisor
            n //= divisor
        divisor += 1
    
    return result

