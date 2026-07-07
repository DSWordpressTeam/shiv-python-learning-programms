# Program 52
# Count Positive and Negative

nums = [3, -2, 7, -1]
pos = len([n for n in nums if n > 0])
neg = len([n for n in nums if n < 0])
print("Positive:", pos, "Negative:", neg)

# Output:
# Positive: 2 Negative: 2
