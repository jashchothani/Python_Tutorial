l1=[]
for i in range(0,5):
    contact=int(input("enter contact number"))
    l1.append(contact)
print(l1) 
search=int(input("enter a num to b searched:"))
if(search in l1):
    print("number found")
else:
    print("number not found")
a=int(input("enter a number to delete"))
l1.remove(a)