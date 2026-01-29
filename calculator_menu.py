while True:
    print("1 for add  2 for sub  3 for mul  4 for div  5 for exit")
    b = int(input("Enter a choice: "))

    if b == 5:
        break

    i = int(input("num 1: "))
    j = int(input("num 2: "))

    if b == 1:
        print(i + j)
    elif b == 2:
        print(i - j)
    elif b == 3:
        print(i * j)
    elif b == 4:
        print(i / j)
    else:
        print("invalid choice")
