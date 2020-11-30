for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Please enter the number of stars you want to print:"))
for i in range(stars):
    print('*', end='')
print()
print("\n")

for i in range(1, stars+1):
    for j in range(1, 1+i):
        print("*", end="")
    print("\n", end="")