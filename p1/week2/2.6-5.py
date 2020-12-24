n = int(input())

dx, dy, x, y = 1, 0, 0, 0
mat = [[None] * n for _ in range(n)]

for i in range(1, n**2 + 1):
    mat[x][y] = i
    nx, ny = x+dx, y+dy
    if 0 <= nx < n and 0 <= ny < n and not mat[nx][ny]:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x+dx, y+dy


for i in range(n):
    for j in range(n):
        print(mat[j][i], end=' ')
    print()