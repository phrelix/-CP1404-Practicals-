list = []
for i in range(5):
    listin = int(input("Enter a value for the list:"))
    list.append(listin)
print(list)

max = max(list)
min = min(list)
sum = sum(list)
length = len(list)
print("The largest number is", max)
print("The smallest number", min)
print("The average of the numbers is", sum/length)
print("First number is ", list[0])
print("Last number is ", list[4])
print(length)

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

check = input("Please enter a password")
if check in usernames:
    print("Access Granted")
else:
    print("Access Denied")