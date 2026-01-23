def main():
    even_num=[]
    odd_num=[]
    num = int(input("Enter the number"))
    for i in range(1,num+1):
        if  i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    i = i+1
    print("Odd Numbers Are: ",odd_num)
    print("Even Numbers Are: ",even_num)


if __name__ == "__main__":
    main()