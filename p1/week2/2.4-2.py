genome = input() + ' '
count = 0
curChar = genome[0]

for i in range(len(genome)):
    if curChar != genome[i]:
        print(curChar, count, sep='', end='')
        count = 0
        curChar = genome[i]
    count += 1