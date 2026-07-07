# Program 35
# Unique Vowels in a Word

word = "programming"
vowels = {ch for ch in word if ch in "aeiou"}
print(sorted(vowels))

# Output:
# ['a', 'i', 'o']
