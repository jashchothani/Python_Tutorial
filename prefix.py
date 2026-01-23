words = ["flower", "flow", "flight"]

# 1. Sort the list alphabetically
words.sort()

first = words[0]
last = words[-1]
prefix = ""

# 2. Compare characters of the first and last word
for i in range(len(first)):
    if first[i] == last[i]:
        prefix += first[i]
    else:
        # Stop as soon as characters don't match
        break

print("Longest Prefix:", prefix)