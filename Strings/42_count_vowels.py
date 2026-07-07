# Program 42
# Count Vowels in a String

s = "programming"
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("Vowels:", count)

# Output:
# Vowels: 3
