import re
fname = input('Enter the file name: ')
if len(fname) < 1: fname = "mbox.txt"
try:
    fhand = open(fname)
except:
    print('File %s cannot be open!' %fname)
    exit()

expression = input('Enter a regular expression: ')
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(expression, line): count += 1

print('{fname} had {count} lines that matched {expression}'.format(fname = fname, count = count, expression = expression))
