import functools
def main():
    value = float(input("Please enter a value to be converted: "))
    x = 0
    while x<1:
        choice = int(input(
            "Please enter if this value is supposed to be converted from celsius to fahrenheit or vice versa:"
            "1= C>F | 2=F>C"))
        if(choice==1):
            x+=1
            value = convertfa(value)
            print("{} degrees Fahrenheit".format(value))
        elif(choice==2):
            x+=1
            value = convertcel(value)
            print("{} degrees Celsius".format(value))
def convertfa(value):
    value = (value *1.8) + 32
    return value

def convertcel(value):
    value = (value-30)/2
    return value

if __name__ == '__main__':
    main()
