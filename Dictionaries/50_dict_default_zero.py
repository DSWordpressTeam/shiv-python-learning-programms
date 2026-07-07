# Program 50
# Build Dictionary with Defaults

letters = "aabbbc"
count = {}
for ch in letters:
    count[ch] = count.get(ch, 0) + 1
print(count)

# Output:
# {'a': 2, 'b': 3, 'c': 1}
