# Program 23
# *args with a Normal Parameter

def greet(msg, *names):
    for name in names:
        print(msg, name)

greet("Hello", "Ram", "Shyam", "Gita")

# Output:
# Hello Ram
# Hello Shyam
# Hello Gita
