# Program 8
# Preserving Metadata with functools.wraps

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet():
    """This function greets."""
    print("Hi")

print(greet.__name__)
print(greet.__doc__)

# Output:
# greet
# This function greets.
