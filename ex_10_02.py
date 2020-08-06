# open a file, press enter to test 'mbox-short.txt'
fname = input('Enter the file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

# creat a dictionary and find the lines start with 'From'
# then save the data as a histogram
count = dict()
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': continue
    # print(words)
    # count[words[5]] = count.get(words[5],0) + 1
    count[words[5][:words[5].find(':')]] = count.get(words[5][:words[5].find(':')],0) + 1

lst = list()
for (hrs, counts) in count.items():
    lst.append((hrs, counts))

lst.sort()
for hrs, counts in lst[:]:
    print(hrs, counts)
