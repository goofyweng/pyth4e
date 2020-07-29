count = 0
total = 0
smallest = None
largest = None
while True:
    line = input('Enter a number: ')
    try:
        number = float(line)
    except:
        if line =='done':
            break
        else:
            print('invalid input')
            continue
    total = total + number
    count = count + 1
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
print('total', total, 'count:', count, 'average:', total/count,'\n')
print('smallest', smallest, 'largest', largest)


# Code: http://www.py4e.com/code3/copytildone2.py
