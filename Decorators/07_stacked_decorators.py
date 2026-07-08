# Program 7
# Multiple (Stacked) Decorators

def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"

print(text())

# Output:
# <b><i>Hello</i></b>
