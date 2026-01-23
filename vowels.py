
word = input("Enter a word: ").lower()

vowels_list = []
consonants_list = []


vowels = "aeiou"

for letter in word:
    
    if letter in vowels:
        vowels_list.append(letter)
    
    elif letter.isalpha():
        consonants_list.append(letter)


print("Vowels:", vowels_list)
print("Consonants:", consonants_list)