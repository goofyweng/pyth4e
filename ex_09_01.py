fname = input('Enter the file name: ')
result = dict()
count = 0
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    words = line.split()
    # print(words)
    for word in words:
        if word in result: continue
        else: result[count] = word
        count = count + 1
# print(result)
vals = list(result.values())
while True:
    cname = input('Enter a word you want to check: ')
    if cname in vals:
        print('True')
    elif cname=='done':
        exit()
    else:
        print('False')
