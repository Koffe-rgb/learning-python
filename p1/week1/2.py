a, b, c = int(input()), int(input()), int(input())

x = max(a, max(b, c))
y = min(a, min(b, c))
z = a + b + c - x - y

print(x, y, z, sep='\n')