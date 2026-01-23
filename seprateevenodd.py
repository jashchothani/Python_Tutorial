
limit = int(input("Enter the ending number: "))

even_numbers = []
odd_numbers = []


for num in range(1, limit + 1):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)