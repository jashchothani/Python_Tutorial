def input_num():
    num = int(input("Enter the Range u want: "))
    return num
def checkoddeve(num):
    if num % 2 == 0 :
        print(f"{num} - Even Number")
    else:
        print(f"{num} - Odd Number")

def main():
    rag = input_num()
    i =1
    while(i<=rag):
        checkoddeve(i)
        i+=1

if __name__ == "__main__":
    main()