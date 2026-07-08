# Program 4
# Decorator Handling Arguments (*args, **kwargs)

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    print("Sum:", a + b)

add(5, 7)

# Output:
# Calling function...
# Sum: 12
