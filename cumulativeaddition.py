numbers = [3, 2, 6, 4, 8, 5]
cumulative_list = []
running_total = 0

for num in numbers:
    
    running_total += num
    
    cumulative_list.append(running_total)

print("Original list:", numbers)
print("Cumulative sum:", cumulative_list)