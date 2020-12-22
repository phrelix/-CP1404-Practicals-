
from programming_language import ProgrammingLanguage

def main():
    my_java = ProgrammingLanguage("Java", "Static", True, 1995)
    my_cpp = ProgrammingLanguage("C++", "Static", False, 1983)
    my_ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    my_python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    my_visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # command / for group commands
    # print(my_java)
    # print(my_cpp)
    # print(my_ruby)
    # print(my_python)
    # print(my_visual_basic)

    proglist= [my_java, my_cpp, my_ruby, my_python, my_visual_basic]
    for i in proglist:
        print(i)

    print("\nThe dynamically typed languages are:")
    for i in proglist:
        if i.is_dynamic():
            print(i.get_name())


    # if my_ruby.is_dynamic():
    #     print("Ruby")
    # if my_python.is_dynamic():
    #     print("Python")

if __name__ == '__main__':
    main()