#   count the the week days in a Email file
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
count = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    # print(words)
    # get the third element in words and count in dictionary
    count[words[2]] = count.get(words[2],0) + 1    
print(count)
print('Done!')
