#!/usr/bin/python3
"""main code base"""


def makeChange(coins, total):
    """main def file for changes"""
    if total <= 0:
        return 0
    check = 0
    ret = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            ret += 1
        if check == total:
            return ret
        check -= i
        ret -= 1
    return -1
