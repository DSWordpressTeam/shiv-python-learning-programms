# Program 27
# Unpacking a List into *args

def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))

# Output:
# 6
