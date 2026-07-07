# Program 31
# Find Minimum in List

nums = [12, 45, 7, 89, 34]
minimum = nums[0]
for n in nums:
    if n < minimum:
        minimum = n
print("Min:", minimum)

# Output:
# Min: 7
