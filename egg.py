fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    #an Easter Egg
    if fname=='na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punkd!')
    else:
        print('File cannot be opened:', fname)
    exit()
count = 0
Data = 0
for line in fhand:
    # line = line.rstrip()
    # if line.startswith('X-DSPAM-Confidence:'):
    #     colpos = line.find(':')
    #     data = line[colpos+1:]
    #     Data=Data+float(data)
        count=count+1

print('There were ',count,'subject lines in ',fname)
