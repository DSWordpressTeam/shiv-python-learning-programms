# Program 39
# Count Even and Odd in List

nums = [1, 2, 3, 4, 5, 6]
even = odd = 0
for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# Output:
# Even: 3 Odd: 3
