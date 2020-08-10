import string
# open a File
fname = input('Enter the file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print('File %s cannot be open! ' %fname)
    exit()

# only keep the letters a-z
count = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.lower()
    words = line.split()

    # start counting each letters in the file
    if len(words) == 0: continue
    for word in words:
        for letter in word:
            count[letter] = count.get(letter,0) +1

# change the order in the decreasing order
lst = list()
for (letter, counts) in count.items():
    lst.append((counts, letter))
lst.sort(reverse  = True)

# print them out!!!
for (counts, letter) in lst:
    print(letter, counts)
