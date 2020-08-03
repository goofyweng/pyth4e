#   count how many messages have come from each email address, and print the dictionary.
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
    # print(words[1])
    # get the third element in words and count in dictionary
    count[words[1]] = count.get(words[1],0) + 1
print(count)
print('Done!')
