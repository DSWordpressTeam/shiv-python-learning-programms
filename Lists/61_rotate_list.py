# Program 61
# Rotate List Left by 1

nums = [1, 2, 3, 4]
nums = nums[1:] + nums[:1]
print(nums)

# Output:
# [2, 3, 4, 1]
