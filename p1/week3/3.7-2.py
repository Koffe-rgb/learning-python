d = int(input())
words = [input().lower() for _ in range(d)]
s = set(words)

l = int(input())
lst = [input().lower().split() for _ in range(l)]

res = set()
for x_list in lst:
    for word in x_list:
        if word not in words:
            res.add(word)

for word in res:
    print(word)