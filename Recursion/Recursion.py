# Common Recursion Examples

"""Power of a number"""


def power(num, n):
    if n == 0:
        return 1
    if n == 1:
        return num
    else:
        if num > 0 or n % 2 == 0:
            return num * power(num, n - 1)
        else:
            return -abs(num * power(num, n - 1))


"""GCD of maximum and minimum number in an array"""


def findGCD(nums):
    if min(nums) == 0:
        return max(nums)
    else:
        return findGCD([min(nums), max(nums) % min(nums)])


"""Decimal to Binary conversion"""


def base2(n):
    if n == 0:
        return 0
    s = ""
    while n != 0:
        s += str(n % 2)
        n = n // 2
    return s[::-1]


"""Factorial of a number"""


def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
