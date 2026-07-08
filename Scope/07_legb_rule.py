# Program 7
# LEGB Rule (Local, Enclosing, Global, Built-in)

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()

# Output:
# local
