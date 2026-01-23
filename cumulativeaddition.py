numbers = [3, 2, 6, 4, 8, 5]
cumulative_list = []
running_total = 0

for num in numbers:
    # Add the current number to the total
    running_total += num
    # Add the new total to our result list
    cumulative_list.append(running_total)

print("Original list:", numbers)
print("Cumulative sum:", cumulative_list)