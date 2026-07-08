# Program 3
# Decorator Printing Before and After

def frame(func):
    def wrapper():
        print("=" * 10)
        func()
        print("=" * 10)
    return wrapper

@frame
def message():
    print("Welcome")

message()

# Output:
# ==========
# Welcome
# ==========
