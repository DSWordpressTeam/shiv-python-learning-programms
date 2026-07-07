# Program 47
# Group Numbers Even/Odd

nums = [1, 2, 3, 4, 5, 6]
groups = {"even": [], "odd": []}
for n in nums:
    if n % 2 == 0:
        groups["even"].append(n)
    else:
        groups["odd"].append(n)
print(groups)

# Output:
# {'even': [2, 4, 6], 'odd': [1, 3, 5]}
