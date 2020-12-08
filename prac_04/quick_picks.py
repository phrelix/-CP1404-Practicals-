from random import choices

number = int(input("How many quick picks?"))
#choice(range(start, stop, step))
randomm = [choices(range(1, 45), k=6) for i in range(number)]


for i, list in enumerate(randomm):
    list.sort()
    #removes brackets
    print(*list)

#found the choices function while trying to understand the ranges of random
