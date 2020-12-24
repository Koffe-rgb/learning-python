lst = [str(i) for i in input().lower().split()]
d = {}

for s in lst:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

for k, v in d.items():
    print(k, v)