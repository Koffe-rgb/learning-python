digits = [int(i) for i in input().split()]

for d in set(digits):
    if digits.count(d) > 1:
        print(d, end=' ')