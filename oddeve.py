def input_num():
    num = int(input("Enter the Number: "))
    return num
def main():
    num = input_num()
    if num % 2 == 0 :
        print(f"{num} is the Even Number")
    else:
        print(f"{num} is the Odd Number")

if __name__ == "__main__":
    main()