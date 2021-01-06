from guitar import Guitar

def main():
    # my_gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    # my_other = Guitar("Standard", 1970, 4372.17)
    #
    # guitarList=[my_gibson, my_other]
    #
    # for i in guitarList:
    #     print("{0} get_age() - Expected {1}. Got {2}".format(i.get_name(), i.get_age(), i.get_age()))
    #
    # for i in guitarList:
    #      print("{0} is_vintage() - Expected {1}. Got {2}".format(i.get_name(), i.is_vintage(), i.is_vintage()))

    guitarList=[]
    print("My guitars!")
    inputname = "None"
    while inputname != "":
        inputname = input("Name: ")
        if inputname == "":
            break
        inputyear = int(input("Year: "))
        inputcost = float(input("Cost: $"))

        guitarList.append(Guitar(inputname, inputyear, inputcost))

        print("{0} ({1}): ${2} added.".format(inputname, inputyear, inputcost))

    print("... snip ...")

    print("These are my guitars:")
    count = 1
    for x, i in enumerate(guitarList, 1):
        if i.is_vintage()==False:
            print("Guitar {0}: {1} ({2}), worth $ {3} ".format(x, i.get_name(), i.get_age(), i.get_cost()))
        else:
            print("Guitar {0}: {1} ({2}), worth $ {3} (vintage)".format(x, i.get_name(), i.get_age(), i.get_cost()))
        count +=1



if __name__ == '__main__':
    main()