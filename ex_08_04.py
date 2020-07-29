fhand = open('romeo.txt')
result=list()
for line in fhand:
    words = line.split()
    # print(words)
    for word in words:
        if word in result: continue
        else: result.append(word)
    result.sort()
print(result)
