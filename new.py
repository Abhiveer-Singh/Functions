# This code is for WINDOWS ONLY
import random
import os
import pyperclip
import webbrowser
import calendar
import time
from datetime import date
all_functions = {
    "sum": "Adds two numbers entered",
    "sub": "Subtracts the first number from the second number",
    "mul": "Multiplies 2 numbers entered",
    "div": "Divides the first value entered by the second value entered",
    "area": "finds the area of rectangle or square".capitalize(),
    "folder": "Creates a folder in the directory specified",
    "remove": "Removes a folder",
    "paste": "Pastes the text copied",
    "copy": "Copies the text typed",
    "all": "Displays all the commands that are there",
    "slope": "calculates the slope of 4 values entered".capitalize(),
    "file": "Makes a new file in the specified directory",
    "link": "Opens the entered link in your default browser",
    "game": "Starts a game that is a surprise for You !!",
    "den": "Finds the density in grams per metre cube",
    "vel": "Finds the velocity in metre per second",
    "acc": "Finds the acceleration from the given values",
    "vol": "Finds the volume",
    "force": "Finds the force from the given mass and acceleration",
    "work": "Finds work done or energy",
    "leap": "Checks if a year is a leap year or not(prints `True` if leap year and `False` if not)",
    "write": "Creates a file and writes it if the user wants to",
    "timer": "Timer for how many ever seconds the user chooses",
    "word": "Counts the amount of words typed",
    "today": "Prints the date in the format: YYYY|MM|DD",
    "youtube": "Opens Youtube in Default Browser",
    "spotify": "Opens Spotify online Player in default browser",
    "medium": "Opens medium on default browser",
    "history": "Prints history",
    "help": "Can tell what each function is used for",
    "instaccount": "takes you to the instagram account you type your default browser in (exact name to be typed)",
    "math": "Displays all mathematical functions",
    "physics": "Displays all Physics Functions",
    "fun": "Displays all miscellaneous(or fun) functions",
    "os": "Displays all functions related to your operating system(windows)",
    "internet": "Displays all functions related to the internet",
    "time": "Displays all time related functions",
    }

maths = {
    "sum": "Adds two numbers entered",
    "sub": "Subtracts the first number from the second number",
    "mul": "Multiplies 2 numbers entered",
    "div": "Divides the first value entered by the second value entered",
    "area": "finds the area of rectangle or square(Same as `mul`)".capitalize(),
    "mathall": "Shows all mathematical functions"
}
physics = {
    "slope": "calculates the slope of 4 values entered".capitalize(),
    "den": "Finds the density in grams per metre cube",
    "vel": "Finds the velocity in metre per second",
    "acc": "Finds the acceleration from the given values",
    "vol": "Finds the volume",
    "force": "Finds the force from the given mass and acceleration",
    "work": "Finds work done or energy",
}
fun = {
    "all": "Displays all the commands that are there",
    "game": "Starts a game that is a surprise for You !!",


}
oss = {
    "folder": "Creates a folder in the directory specified",
    "remove": "Removes a folder",
    "file": "Makes a new file in the specified directory",
    "write": "Creates a file and writes it if the user wants to",
}
internet = {
    "youtube": "Opens Youtube in Default Browser",
    "spotify": "Opens Spotify online Player in default browser",
    "medium": "Opens medium on default browser",
    "instaccount": "takes you to the instagram account you type your default browser in (exact name to be typed)",
    "link": "Opens the entered link in your default browser",
}
times = {
    "timer": "Timer for how many ever seconds the user chooses",
    "today": "Prints the date in the format: YYYY|MM|DD",
}
everything = [maths, physics, fun, oss, internet, times]


def favourites():
    favourite = []


def account():
    insta_name = input("Type the name of the instagram account you want to go to (exact name): ")
    webbrowser.open_new_tab("https://www.instagram.com/{0}".format(insta_name))


def to_do():
    name = input("Enter the name of your file (including extension): ")
    directory = input("Enter the directory where you want to store your file\n1.Documents\n2.Downloads\n3.Desktop\n: ")
    path = f"C:/Users/abhiv/{directory}/{name}"
    file = open(path, 'a')
    num = int(input("How things do you want to put on this to-do list ?(number): "))
    n = 0
    while n != num:
        n += 1
        la = input("Type Here: ")
        file.write(la + "\n")
    file.close()


def assist():
    print("Type the keyword which you want help with: ")
    for x, y in enumerate(all_functions.keys()):
        print(x + 1, y)
    key = input("Type Here: ")
    if key in all_functions.keys():
        print(all_functions[key])


def medium():
    webbrowser.open_new_tab("https://www.medium.com")


def youtube():
    webbrowser.open_new_tab("https://www.youtube.com")


def spotify():
    webbrowser.open_new_tab("open.spotify.com")


def today():
    print(f"The Date Today is: {date.today()}")


def timer():
    secs = int(input("Enter in Seconds: "))
    time.sleep(secs)


def write():
    name = input("What do You want to name your file: ")
    dir = input(f"Which directory do you want to create {name} in ?\n1.Documents\n2.Downloads\n3Desktop\n: ")
    path = f"C:/Users/abhiv/{dir}/{name}"
    file = open(path, 'w')
    enter = input("Do You want to write something to the file?(Yes or No): ")
    if enter == "no".casefold():
        pass
    elif enter == "yes".casefold():
        con = input("Type the content of the file here: ")
        file.write(con)
    file.close()


def leap():
    leap = int(input("Enter year to be checked: "))
    print(calendar.isleap(leap))


def word():
    print("Enter the words to count below")
    words = input(": ")
    print(len(words.split()))


def link():
    me = input("Enter url of website")
    webbrowser.open("https://{}".format(me))


def func():
    for a, b in (all_functions.items()):
        print(a, ": ", b)


def game():
    a = int(input("Enter a range (first number): "))
    b = int(input("Enter a range (second number): "))
    me = random.randint(a, b)
    enter = int(input("Guess the number: "))
    while enter != me:
        enter = int(input("Guess the number: "))
        if enter > me:
            print("Guess Lower")
        elif enter < me:
            print("Guess Higher")
        elif enter == me:
            print("Congratulations! You got the right number")


def slope():
    y2 = float(input("Enter y2: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    x1 = float(input("Enter x1: "))
    one = y2 - y1
    two = x2 - x1
    print(one / two)


def paste():
    print(pyperclip.paste)


def copy():
    cop = pyperclip.copy(input("Type here: "))
    print(f"{cop} copied to os clipboard!")


def den():
    mass = float(input("Type mas in grams: "))
    volu = float(input("Type volume in metre cube: "))
    print(f"Density is {mass / volu} ")


def speed():
    dis = float(input("Type the distance in metres: "))
    tim = float(input("Type time in second: "))
    print("S    peed is {} m per second".format(dis / tim))


def acc():
    velocity = float(input("Type the velocity in metre per second: "))
    time = float(input("Type the time in seconds: "))


def vol():
    side = int(input("Type the measurement of one side here: "))
    print(f"The volume is {pow(side, 3)}")


def force():
    ma = float(input("Type the mass in grams: "))
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
    print(f"Torque or moment of force is equal to {fo * dista} N m")


def power():
    wor = float(input("Type work in Joule: "))
    tim = float(input("enter time in seconds: "))
    print(f"Power is equal to {wor / tim} J per second or Watt")


def pressure():
    fo = float(input("Type force in N: "))
    are = float(input("Type area in metre square: "))
    print(f"The pressure is {fo / are} N per metre square")


def frequency():
    period = float(input("Type time period in seconds"))
    print(f"Frequency is equal to {1 / period} Hertz or second raised to -1")


def charge():
    current = float(input("Type current in ampere: "))
    time = float(input("Type time in second: "))
    print(f"Electric charge is equal to {current * time} A s or C")


def area():
    shape = input("Which shape's area is to be found ?")
    if shape == "rectangle".casefold():
        one = float(input("Type length: "))
        two = float(input("Type breadth: "))
        print(one * two)
    elif shape == "square".casefold():
        la = float(input("Type side of square"))
        print(la * la)
    elif shape == "triangle".casefold():
        base = float(input("Enter length of base in centimetres: "))
        height = float(input("Enter the length of height in centimetres: "))
        print("The area of this triangle is ", (base * height) / 2)


def div():
    print("You have chosen division")
    two = float(input("Type the second number: "))
    one = float(input("Type the first number: "))
    res = two / one
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


def add():
    print("You have chosen addition")
    a = float(input("Type the first number: "))
    b = float(input("Type the first number: "))
    print(a + b)


def remove():
    print("The only ones allowed are:\n1.Documents\n2.Downloads\n3.Desktop\nIn which directory is Your file in ?")
    pla_2 = input("Type here: ")
    fold_2 = input("What is the name of Your file ?")
    os.rmdir(f"C:/Users/abhiv/{pla_2}/{fold_2}")
    print(f"File: \"{fold_2}\" removed")


def folder():
    print("The only ones allowed are:\n1.Documents\n2.Downloads\n3.Desktop\nIn which directory is Your file in ?")
    fil = input("Type Here: ")
    place = input("What would You like to name Your folder?: ")
    os.mkdir(f"C:/Users/abhiv/{fil}/{place}")


bash = []

print("Welcome")

entry = input("PRESS ENTER")
while entry != "exit":
    entry = input(">")
    bash.append(entry)
    if entry == "exit".casefold():
        break
    elif entry == "sum".casefold():
        add()
        # all_func.append("sum")
        # print("Addition")
    elif entry == "sub".casefold():
        sub()
    elif entry == "mul".casefold():
        mul()
    elif entry == "div".casefold():
        div()
    elif entry == "area".casefold():
        area()
    elif entry == "":
        pass
    elif entry == "folder".casefold():
        folder()
    elif entry == "remove".casefold():
        remove()
    elif entry == "paste":
        print(pyperclip.paste())
    elif entry == "copy":
        copy()
    elif entry == "all".casefold():
        for i, j in enumerate(all_functions):
            print(i + 1, j, all_functions[j], sep=". ")
    elif entry == "all".casefold():
        func()
    elif entry == "slope".casefold():
        slope()
    elif entry == "folder".casefold():
        folder()
    elif entry == "game".casefold():
        game()
    elif entry == "den".casefold():
        den()
    elif entry == "vol".casefold():
        vol()
    elif entry == "speed":
        speed()
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
    elif entry == "link".casefold():
        link()
    elif entry == "frequency".casefold():
        frequency()
    elif entry == "file":
        write()
    elif entry == "leap":
        leap()
    elif entry == "timer":
        timer()
    elif entry == "word":
        word()
    elif entry == "today":
        today()
    elif entry == "acc":
        acc()
    elif entry == 'spotify':
        spotify()
    elif entry == "youtube":
        youtube()
    elif entry == "history":
        for i in bash:
            print(i)
    elif entry == "medium":
        medium()
    elif entry == "help":
        assist()
    elif entry == "to do list":
        to_do()
    elif entry == "instaccount":
        account()
    elif entry == "math":
        for z in maths.keys():
            print(z, maths[z], sep=": ")
    elif entry == "physics":
        for x in physics.keys():
            print(x, physics[x], sep=": ")
    elif entry == "os":
        for a in oss.keys():
            print(a, oss[a], sep=": ")
    elif entry == "internet":
        for b in internet.keys():
            print(b, internet[b], sep=": ")
    elif entry == "time":
        for t in times.keys():
            print(t, times[t], sep=": ")
    else:
        print(f"could not understand what {entry} meant.Try something from the list below")
        func()
