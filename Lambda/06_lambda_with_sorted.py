# Program 6
# Lambda as sorted() Key

pairs = [(1, "one"), (3, "three"), (2, "two")]
pairs.sort(key=lambda x: x[0])
print(pairs)

# Output:
# [(1, 'one'), (2, 'two'), (3, 'three')]
