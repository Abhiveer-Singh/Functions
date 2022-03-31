print("Hi")
name = input("Enter the name of your file (including extension): ")
directory = input("Enter the directory where you want to store your file\n1.Documents\n2.Downloads\n3.Desktop")
path = f"C:/Users/abhiv/{directory}/{name}"
file = open(path, 'a')
num = int(input("How things do you want to put on this to-do list ?(number): "))
n = 0
while n != num:
    n += 1
    la = input("Type Here: ")
    file.write(la+ "\n")
file.close()
