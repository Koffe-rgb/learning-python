digits = [int(i) for i in input().split()]

if len(digits) == 1:
    print(digits[0])
else:
    for i in range(len(digits)):
        print(digits[i - 1] + digits[(i + 1) - len(digits)], end=' ')