# Program 9
# Decorator with Parameters (Decorator Factory)

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()

# Output:
# Hello
# Hello
# Hello
