from math import factorial
import itertools

def primes():
    i = 1
    while True:
        i += 1
        f = factorial(i - 1)
        if (f + 1) % i == 0:
            yield i



print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
