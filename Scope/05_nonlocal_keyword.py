# Program 5
# nonlocal Keyword

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print("x after inner:", x)

outer()

# Output:
# x after inner: 20
