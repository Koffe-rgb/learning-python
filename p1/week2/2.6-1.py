sum = 0
dsum = 0

while True:
    a = int(input())
    dsum += a * a
    sum += a
    if sum == 0:
        break

print(dsum)