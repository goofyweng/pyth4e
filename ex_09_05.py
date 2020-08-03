#   count how many messages have come from each email address, and print the dictionary.
fname = input('Enter the file name: ')
#  to make test process faster...
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
count = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    #  records the domain name (instead of the address) where the message -
    # -was sent from instead of who the mail came from
    # the second element(string) in the list is the whole email address
    # find the index of '@' in the second element(string)  than +1
    # words[1][words[1].find('@')+1:] == string[start:end]
    # print(words[1][words[1].find('@')+1:])
    count[words[1][words[1].find('@')+1:]] = count.get(words[1][words[1].find('@')+1:],0) + 1
print(count)
