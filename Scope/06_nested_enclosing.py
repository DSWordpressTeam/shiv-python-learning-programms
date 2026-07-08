# Program 6
# Nested Function Accessing Enclosing Scope

def outer():
    msg = "Hello from outer"
    def inner():
        print(msg)
    inner()

outer()

# Output:
# Hello from outer
