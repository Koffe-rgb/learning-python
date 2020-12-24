from functools import reduce

s = reduce(lambda x, y: x + y, [int(i) for i in input().split()])
print(s)