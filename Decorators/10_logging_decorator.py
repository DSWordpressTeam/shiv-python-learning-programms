# Program 10
# Logging Decorator

def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__, "with", args)
        result = func(*args, **kwargs)
        print("Returned:", result)
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

multiply(4, 5)

# Output:
# Calling: multiply with (4, 5)
# Returned: 20
