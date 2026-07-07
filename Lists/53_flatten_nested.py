# Program 53
# Flatten Nested List

nested = [[1, 2], [3, 4], [5]]
flat = [x for sub in nested for x in sub]
print(flat)

# Output:
# [1, 2, 3, 4, 5]
