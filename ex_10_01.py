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
    count[words[1]] = count.get(words[1],0) + 1

# creat a list to store the data and shift the email & val
lst = list()
for (email, val) in count.items():
    lst.append((val, email))
# Then sort the list in reverse order
lst.sort(reverse = True)
# print out the person who has the most commits
for (val, email) in lst[:1]:
    print(email, val)
