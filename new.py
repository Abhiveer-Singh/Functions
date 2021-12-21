# This code is for WINDOWS ONLY

import os
import pyperclip
# add the formula and functionality of slope


def func():
    for i, j in enumerate(all_func):
        print(i+1, j)


# def lists(): #this function is not ready yet and needs to be amended.Everything else seems fine and is working fine
#     # l = input("JUST PRESS ENTER")   Keep Thinking.Make a CLI and do shit and be successful
#     # while l != "exit":
#     #     l = input(">")
#     #     t = []
#     #     t.append(l)
#     #     # t.remove("exit")
#     #     for i in t:
#     #         print(i)
#     me = input("(don't)type here")
#     while me != "exit":
#         me = input(">")
#         t = []
#         t.append(me)
#         for i in t:
#             print(i)
# lists()

# sum sub mul div area folder remove paste copy all slope file
fun = {
    "sum": "Adds two numbers entered",
    "sub": "Subtracts the first number from the second number",
    "mul": "Multiplies 2 numbers entered",
    "div": "Divides the first value entered by the second value entered",
    "area": "finds the area of rectangle or square(Same as `mul`)".capitalize(),
    "folder": "Creates a folder in the directory specified",
    "remove": "Removes a file/folder",
    "paste": "Pastes the text copied",
    "copy": "Copies the text typed",
    "all": "Displays all the commands that can be typed",
    "slope": "calculates the slope of 4 values entered".capitalize(),
    "file": "Makes a new file in the specified directory"
    }


def slope():
    y2 = float(input("Enter y2: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    x1 = float(input("Enter x1: "))
    one = y2 - y1
    two = x2 - x1
    print(one/two)


def area():
    shape = input("Which shape's area is to be found ?")
    if shape == "rectangle".casefold():
        one = float(input("Type length: "))
        two = float(input("Type breadth: "))
        print(one * two)
    elif shape == "square".casefold():
        la = float(input("Type side of square"))
        print(la * la)


def div():
    print("You have chosen division")
    two = float(input("Type the second number: "))
    one = float(input("Type the first number: "))
    res = two/one
    if res == 0:
        print("Not defined")
    else:
        print(res)


def mul():
    print("You have chosen multiplication")
    e = float(input("Type the first number: "))
    f = float(input("Type the second number: "))
    print(e * f)


def sub():
    print("You have chosen subtraction")
    c = float(input("Type the first number: "))
    d = float(input("Type the second number: "))
    print(c - d)


print("Welcome")


def add():
    print("You have chosen addition")
    a = float(input("Type the first number: "))
    b = float(input("Type the first number: "))
    print(a + b)


entry = input("PRESS ENTER")
while entry != "exit":
    entry = input(">")
    all_func = ("sum", "subtract", "multiplication", "division", "area", "paste", "copy", "all", "folder",
                "remove")
    if entry == "exit".casefold():
        break
    elif entry == "sum".casefold():
        add()
        # all_func.append("sum")
        # print("Addition")
    elif entry == "sub".casefold():
        sub()
        # all_func.append("subtract")
        # print("Subtraction")
    elif entry == "mul".casefold():
        # print("Multiplication")
        mul()
        # all_func.append("multiplication")
    elif entry == "div".casefold():
        # print("Division")
        div()
        # all_func.append("division".title())
    elif entry == "area".casefold():
        area()
    elif entry == "":
        pass
    elif entry == "folder".casefold():
        print("The only ones allowed are:\n1.Documents\n2.Downloads\n3.Desktop")
        pla = input("Where do you want to store Your files ?")
        fold = input("what is the name of Your file ?")
        os.mkdir(f"C:/Users/abhiv/{pla}/{fold}")
    elif entry == "remove".casefold():
        print("The only ones allowed are:\n1.Documents\n2.Downloads\n3.Desktop\nIn which directory is Your file in ?")
        pla_2 = input("Type here: ")
        fold_2 = input("What is the name of Your file ?")
        os.rmdir(f"C:/Users/abhiv/{pla_2}/{fold_2}")
        print(f"File: \"{fold_2}\" removed")
    elif entry == "paste":
        print(pyperclip.paste())
    elif entry == "copy":
        cop = pyperclip.copy(input("Type here: "))
        print(f"{cop} copied to os clipboard!")
    # elif entry == f"help --{entry}":
    #     if entry in
    # elif entry == "list":
    #     lists()
    elif entry == "all".casefold():
        for i, j in enumerate(fun):
            print(i+1, j, fun[j], sep=". ")
    elif entry == "all".casefold():
        # print("The following are the functions You can perform")
        # print(all_func)
        func()
    elif entry == "slope".casefold():
        slope()
    elif entry == "file".casefold():
        print("The only ones allowed are:\n1.Documents\n2.Downloads\n3.Desktop\nIn which directory is Your file in ?")
        fil = input("Type Here: ")
        place = input("Type the name of the file: ")
        os.mkdir(f"C:/Users/abhiv/{fil}/{place}")
    else:
        print(f"could not understand what {entry} meant.Try something from the list below")
        func()
    # for i in t:
    #     print(t)
    # entry = input(">")
