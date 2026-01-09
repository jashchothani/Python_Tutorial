def reversenum():
    n= int(input("Enter the number: "))
    num = 0
    ogn = n
    while(n!=0):
        d = n%10
        num = num*10+d
        n = n//10
    print(f"og: {ogn} reversed: {num}")
def main():
    reversenum()
if __name__ == "__main__":
    main()