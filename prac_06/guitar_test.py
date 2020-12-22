from guitar import Guitar

def main():
    my_gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    my_other = Guitar("Standard", 1970, 4372.17)

    guitarList=[my_gibson, my_other]

    for i in guitarList:
        print("{0} get_age() - Expected {1}. Got {2}".format(i.get_name(), i.get_age(), i.get_age()))

    for i in guitarList:
         print("{0} is_vintage() - Expected {1}. Got {2}".format(i.get_name(), i.is_vintage(), i.is_vintage()))





if __name__ == '__main__':
    main()