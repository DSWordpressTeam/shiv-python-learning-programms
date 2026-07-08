# Program 6
# Function Calling Another Function

def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print("Result:", sum_of_squares(3, 4))

# Output:
# Result: 25
