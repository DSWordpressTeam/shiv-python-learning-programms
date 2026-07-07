# Program 68
# Cumulative Sum

nums = [1, 2, 3, 4]
result = []
total = 0
for n in nums:
    total += n
    result.append(total)
print(result)

# Output:
# [1, 3, 6, 10]
