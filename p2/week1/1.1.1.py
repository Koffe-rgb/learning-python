from functools import reduce

n = int(input())
nums = [int(input()) for i in range(n)]
sum_n = reduce(lambda x,y: x+y, nums)
print(sum_n)