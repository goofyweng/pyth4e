fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    # if words[0] != 'From' : continue
    print(words[1])
    count = count+1
print('There were %d lines in the file with From as the first word'%count)
