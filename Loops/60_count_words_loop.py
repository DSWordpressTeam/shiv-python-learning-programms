# Program 60
# Count Words in Sentence

sentence = "learning python is fun"
count = 1
for ch in sentence:
    if ch == " ":
        count += 1
print("Words:", count)

# Output:
# Words: 4
