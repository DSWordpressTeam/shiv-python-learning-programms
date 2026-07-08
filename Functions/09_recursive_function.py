# Program 9
# Recursive Function (Factorial)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))

# Output:
# Factorial: 120
