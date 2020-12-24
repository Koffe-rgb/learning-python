mat = []

while True:
    s = str(input())
    if s == 'end':
        break
    mat.append([int(i) for i in s.split()])

li = len(mat)
lj = len(mat[0])

mat2 =  [[sum([mat[i][j+1-lj], mat[i][j-1], mat[i+1-li][j], mat[i-1][j]]) for j in range(lj)] for i in range(li)]

for i in range(li):
    for j in range(lj):
        print(mat2[i][j], end=' ')
    print()