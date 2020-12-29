s = str(input())
a = str(input())
b = str(input())

i = 0
while True:
    if a in s and a in b or i > 1000:
        print('Impossible')
        break
    elif a in s:
        s = s.replace(a, b)
        i += 1
    else:
        print(i)
        break
