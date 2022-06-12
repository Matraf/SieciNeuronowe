import math
import numpy


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def random(min, max):
    num = math.floor(numpy.random.uniform(0, 1) * (max + 1 - min) + min)
    if num == 1:
        return random(min, max)
    return num


def factorization(n):
    t = n ** 2
    while True:
        a = random(1, n)

        tempGCD = gcd(n, a)
        if tempGCD > 1:
            return tempGCD
        r = 0
        while (a ** r - 1) % n == 0 and a ** r < t:
            r = r + 1
        if gcd(n, a ** (r / 2) - 1) > 1:
            return tempGCD
        if gcd(n, a ** (r / 2) + 1) > 1:
            return tempGCD


print("factorization of 12:\t" + str(factorization(12)))
print("factorization of 57:\t" + str(factorization(57)))
print("factorization of 91:\t" + str(factorization(91)))
print("factorization of 143:\t" + str(factorization(143)))
print("factorization of 1737:\t" + str(factorization(1737)))
print("factorization of 1859:\t" + str(factorization(1859)))
print("factorization of 13843:\t" + str(factorization(13843)))
