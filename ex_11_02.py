import re
fname = input('Enter file: ')
if len(fname) < 1: fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File {} cannot be open!'.format(fname) )
    exit()

data = list()
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]*)', line)
    if len(x) > 0:
        # the x is a list of string with only one element
        #  change the element into a list of lists
        data.append([float(i) for i in x])

# the current data is still a list of lists
# if we want to use sum()
# we need to change the data into a list of floats
data = sum(data,[])
print(int(sum(data)/len(data)))
