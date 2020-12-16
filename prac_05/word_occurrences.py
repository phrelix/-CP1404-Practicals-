def main():
    str = input("Text: ")
    textstring(str)
def textstring(str):
    str = str.split()
    final = []
    for i in str:
        if i not in final:
            final.append(i)
    for i in range(0, len(final)):
        print(final[i], ':', str.count(final[i]))
if __name__ == "__main__":
    main()