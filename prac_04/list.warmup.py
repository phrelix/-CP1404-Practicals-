numbers = [3, 1, 4, 1, 5, 9, 2]

'''
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = 2, 9, 5, 1, 3, 1, 3
numbers[3:4] = 1, 5
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]
Dont understand the rest.

    Change the first element of numbers to "ten" (the string, not the number 10)
    Change the last element of numbers to 1
    Get all the elements from numbers except the first two (slice)
    Check if 9 is an element of numbers

'''

numbers[0]= "ten"
numbers[6]= 1
print(numbers[2:])
print("")
for element in numbers:
    print(element, end='')
    if element==9:
        print("9 is in the numbers")