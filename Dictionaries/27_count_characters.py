# Program 27
# Count Character Frequency

word = "banana"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Output:
# {'b': 1, 'a': 3, 'n': 2}
