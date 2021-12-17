# l = [1, 2, 3, 4, 5, 6 ,7]
# for i in l:print(l)
# h_letters = [ letter for letter in 'human' ]
# print( h_letters)
#
# me = [l for l in sorted('I am Awesome')]
# print(me)


tac = ("\t1 | 2 | 3\n"
       "\t4 | 5 | 6\n"
       "\t7 | 8 | 9")
print(tac)
done = []
while len(done) == 0:
    X1 = int(input("X: "))
    if X1 == 1:
        tac = (f"\tX|  | \n"
               "\t |  | \n"
               "\t |  | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    X1 = int(input("X: "))
    if X1 == 2:
        tac = (f"\t| X | \n"
               "\t |  | \n"
               "\t |  | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    X1 = int(input("X: "))
    if X1 == 3:
        tac = (f"\t |  | X\n"
               "\t |  | \n"
               "\t |  | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    X1 = int(input("X: "))
    if X1 == 4:
        tac = (f"\t|  | \n"
               "\tX |  | \n"
               "\t |  | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    if X1 == 5:
        tac = (f"\t|  | \n"
               "\t | X | \n"
               "\t |  | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    if X1 == 6:
        tac = (f"\t|  | \n"
               "\t |  | X\n"
               "\t |  | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    if X1 == 7:
        tac = (f"\t|  | \n"
               "\t |  | \n"
               "\tX |  | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    if X1 == 8:
        tac = (f"\t|  | \n"
               "\t |  | \n"
               "\t | X | ")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
    if X1 == 9:
        tac = (f"\t|  | \n"
               "\t |  | \n"
               "\t |  | X")
        print(tac)
        done.append(X1)
    print(done)
    O1 = input("O: ")
