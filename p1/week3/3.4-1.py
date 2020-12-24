line = ''
with open('c:\\Users\\Nickolay\\Desktop\learning-python\\p1\\week3\\3.4-1-input.txt', 'r') as fis:
    line = fis.readline()
    line += ' '

curChar = ''
curDigit = '0'
result = ''
for char in line:
    if char.isalpha() or char.isspace():
        result += str(curChar * int(curDigit))
        curDigit = ''
        curChar = char
    else:
        curDigit += char

with open('c:\\Users\\Nickolay\\Desktop\learning-python\\p1\\week3\\3.4-1-output.txt', 'w') as fos:
    fos.write(result)
    print(result)