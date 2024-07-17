x = int(input("X axis len: "))
y = int(input("Y axis len: "))
mode = int(input("Choose a mode: mid, end, start (0, 1, 2): "))

match mode:
    case 0:
        for c in range(0, y):
            if c == int(y/2):
                print("|" + "_"*x*2)
            else:
                print("|")


    case _:
        print("Invalid option!!!")