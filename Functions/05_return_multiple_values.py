# Program 5
# Function Returning Multiple Values

def calc(a, b):
    return a + b, a - b, a * b

s, d, p = calc(10, 4)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)

# Output:
# Sum: 14
# Difference: 6
# Product: 40
