import os


name = input("What do You want to name your file: ")
dir = input(f"Which directory do you want to create {name} in ?\n1.Documents\n2.Downloads\n3Desktop\n: ")
path = f"C:/Users/abhiv/{dir}/{name}"
file = open(path, 'w')
# entry = input("Type Here: ")
# while entry != "PRESS ENTER":
entry = input("> ")
file.write(entry+"\n")
file.close()
x = open(file="{file}", newline='')
for row in file:
    print(row)