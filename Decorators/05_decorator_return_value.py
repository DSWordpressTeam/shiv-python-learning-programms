# Program 5
# Decorator Returning a Value

def double(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double
def get_number():
    return 10

print(get_number())

# Output:
# 20
