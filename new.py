# This code is for WINDOWS ONLY
import random
import os
import pyperclip

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


def func():
    for a, b in enumerate(all_func):
        print(a + 1, b)


def game():
    a = int(input("Enter a range (first number): "))
    b = int(input("Enter a range (second number): "))
    me = random.randint(a, b)
    enter = int(input("Guess the number: "))
    while enter != me:
        enter = int(input("Guess the number: "))
        if enter == me:
            print("Congratulations! You got a number")


def slope():
    y2 = float(input("Enter y2: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    x1 = float(input("Enter x1: "))
    one = y2 - y1
    two = x2 - x1
    print(one/two)


def den():
    mass = float(input("Type mas in grams: "))
    volu = float(input("Type volume in metre cube: "))
    print(f"Density is {mass*volu} ")


def vel():
    dis = float(input("Type the distance in metres: "))
    tim = float(input("Type time in second: "))
    print("Velocity is {} m per second".format(dis/tim))


def acc():
    velocity = float(input("Type the velocity in metre per second: "))
    time = float(input("Type the time in seconds: "))


def vol():
    side = int(input("Type the measurement of one side here: "))
    print(f"The volume is {pow(side, 3)}")


def force():
    ma = float(input("Type the mass in grams "))
    accelerate = float(input("Type acceleration in metre per second square: "))
    print(f"Force = {ma * accelerate} Newton")


def work():
    forc = float(input("Type the force in Newton: "))
    displace = float(input("Type the displacement in metre: "))
    print(f"Work done or energy is equal to {forc * displace} Joule")


def mom():
    mass = float(input("Enter mass in kilograms: "))
    velo = float(input("Enter velocity in metre per second: "))
    print(f"Momentum is equal to {mass * velo} N s")


def torque():
    fo = float(input("Type force in N: "))
    dista = float(input("Type distance in metre: "))
    print(f"Torque or moment of force is equal to {fo *dista} N m")


def power():
    wor = float(input("Type work in Joule: "))
    tim = float(input("enter time in seconds: "))
    print(f"Power is equal to {wor/tim} J per second or Watt")


def pressure():
    fo = float(input("Type force in N: "))
    are = float(input("Type area in metre square: "))


def frequency():
    period = float(input("Type time period in seconds"))
    print(f"Frequency is equal to {1/period} Hertz or second raised to -1")


def charge():
    current = float(input("Type current in ampere: "))
    time = float(input("Type time in second: "))
    print(f"Electric charge is equal to {current*time} A s or C")


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
    elif entry == "game".casefold():
        pass # random number game (That one)
    elif entry == "den".casefold():
        den()
    elif entry == "vol".casefold() or "speed".casefold():
        vol()
    elif entry == "force".casefold():
        force()
    elif entry == "work".casefold():
        work()
    elif entry == "mom".casefold():
        mom()
    elif entry == "torque".casefold():
        torque()
    elif entry == "power".casefold():
        power()
    elif entry == "pressure".casefold():
        pressure()
    elif entry == "charge".casefold():
        charge()
    else:
        print(f"could not understand what {entry} meant.Try something from the list below")
        func()