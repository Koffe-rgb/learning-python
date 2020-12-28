from math import factorial

def C(n, k):
    return int(factorial(n) / factorial(k) / factorial(n - k))

print(C(*[int(i) for i in input().split()]))