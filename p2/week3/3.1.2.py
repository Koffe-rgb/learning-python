s = str(input())
t = str(input())

c = 0

for i in range(len(s)):
    if s.startswith(t, i):
        c += 1

print(c)