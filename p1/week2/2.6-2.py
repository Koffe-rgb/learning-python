n = int(input())
s = []

for i in range(1, n + 1):
    s += [str(i)] * i

a = (' '.join(s[:n]))
print(a)
