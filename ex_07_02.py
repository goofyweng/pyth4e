fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
Data = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        colpos = line.find(':')
        data = line[colpos+1:]
        Data=Data+float(data)
        count=count+1

print('Average spam confidenc:',Data/count)
