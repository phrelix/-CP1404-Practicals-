def valid_password(password):
    S = "*"
    p_count = 0
    length = len(password)
    if length <= 0:
        return False

    for char in password:
        if char.isupper():
            p_count +=1
        if char.islower():
            p_count +=1
    if p_count <0:
        return False
    for i in range(p_count):
        print(S, end='')
    return True
def main():
    password = input("Enter password: ")
    while not valid_password(password):
        print("Invalid Password")
        password = input("Enter a valid password: ")

if __name__ == '__main__':
    main()
