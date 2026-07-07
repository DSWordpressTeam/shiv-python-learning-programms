# Program 54
# Group Words by First Letter

words = ["apple", "banana", "avocado", "berry"]
groups = {}
for w in words:
    groups.setdefault(w[0], []).append(w)
print(groups)

# Output:
# {'a': ['apple', 'avocado'], 'b': ['banana', 'berry']}
