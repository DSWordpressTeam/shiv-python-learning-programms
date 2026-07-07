# Program 55
# Count Positive & Negative

nums = [3, -2, 7, -8, 0, 4]
pos = neg = 0
for n in nums:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
print("Positive:", pos, "Negative:", neg)

# Output:
# Positive: 3 Negative: 2
