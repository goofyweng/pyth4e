numlist = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    try:
        num = float(inp)
    except:
        print('Not a number, be serious!')
        continue
    numlist.append(num)

print('Maximum:',max(numlist))
print('Minimum:',min(numlist))
