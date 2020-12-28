path = 'c:\\Users\\Nickolay\\Desktop\\learning-python\\p1\\week3\\3.4-2-input.txt'
d = {}

with open(path, 'r') as fis:
    for line in fis:
        words = [str(l) for l in line.lower().strip().split()]
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

maxValue = max(d.values())
res = [str(k) for k in d.keys() if d[k] == maxValue]
print(min(res), maxValue)