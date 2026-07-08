# Program 1
# Simple Decorator

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def hello():
    print("Hello!")

hello = decorator(hello)
hello()

# Output:
# Before function
# Hello!
# After function
