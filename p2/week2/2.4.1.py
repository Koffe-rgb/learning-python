
pathr = 'c:\\Users\\Nickolay\\Desktop\\learning-python\\p2\\week2\\2.4.1.input.txt'
pathw = 'c:\\Users\\Nickolay\\Desktop\\learning-python\\p2\\week2\\2.4.1.output.txt'

with open(pathr, 'r') as fis, open(pathw, 'w') as fos:
    lines = [line.strip() for line in fis]
    revlines = '\n'.join(lines[::-1])
    for line in revlines:
        fos.write(line)