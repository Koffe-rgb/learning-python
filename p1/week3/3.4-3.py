from functools import reduce

pathr = 'c:\\Users\\Nickolay\\Desktop\\learning-python\\p1\\week3\\3.4-3-input.txt'
pathw = 'c:\\Users\\Nickolay\\Desktop\\learning-python\\p1\\week3\\3.4-3-output.txt'

avgs = [0, 0, 0]
n = 0

with open(pathr, 'r', encoding="utf8") as fis:
    with open(pathw, 'w') as fos:
        for line in fis:
            n += 1
            words = [str(l) for l in line.strip().split(';')][1:]
            avg = reduce(lambda x, y: int(x)+int(y), words) / len(words)
            fos.write(str(avg) + '\n')

            for i in range(len(words)):
                avgs[i] += int(words[i])
        for i in range(len(avgs)):
            fos.write(str(avgs[i] / n) + ' ')
        fos.write('\n')
