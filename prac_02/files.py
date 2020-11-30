name = input("Please enter your name: ")
nfile = open("name.txt", "w")
nfile.write(name)
nfile.close()

nfile = open("name.txt", "r")
print(nfile.read())
nfile.close()

file = open("name.txt", "r")
print("Your name is", file.read())
file.close()

numberfile = open("numbers.txt", "r")
a = 0
x = 1
while(x<3):
    values = int(numberfile.readline())
    a = a + values
    x+=1
print(a)
numberfile.close()
#this worked but was quite athe challenge


#number 4
printloop = open("numbers.txt", "r")
line = printloop.readline()
while line:
    print(line)
    line = printloop.readline()
numberfile.close()
