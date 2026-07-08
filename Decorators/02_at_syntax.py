# Program 2
# Decorator with @ Syntax

def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def show():
    print("Inside show")

show()

# Output:
# Start
# Inside show
# End
