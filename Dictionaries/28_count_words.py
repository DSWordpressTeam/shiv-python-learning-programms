# Program 28
# Count Word Frequency

text = "a b a c b a"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)

# Output:
# {'a': 3, 'b': 2, 'c': 1}
