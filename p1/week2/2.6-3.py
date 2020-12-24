lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
else:
    for i, item in enumerate(lst):
        if item == x:
            print(i, end=' ')