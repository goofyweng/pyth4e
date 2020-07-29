#Print a string from backward
index = 1
fruit = input('enter a fruit:')
while index <=  len(fruit) :
    letter = fruit[ len(fruit) - index ]
    print(letter)
    index = index + 1
