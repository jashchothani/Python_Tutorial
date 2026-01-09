def main():
    age = int(input("Enter the Age: "))

    if age <= 0:
        print("Age Error!! Enter Valid Age!!!!")
    elif age < 18:
        print("Teenager")
    elif age < 60:
        print("Adult")
    else:
        print("Senior citizen")


if __name__ == "__main__":
    main()
