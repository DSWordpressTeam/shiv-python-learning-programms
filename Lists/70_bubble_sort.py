# Program 70
# Bubble Sort a List

nums = [5, 2, 8, 1, 4]
for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)

# Output:
# [1, 2, 4, 5, 8]
