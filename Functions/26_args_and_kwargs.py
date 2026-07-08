# Program 26
# Combining *args and **kwargs

def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, name="Ravi", age=40)

# Output:
# Args: (1, 2)
# Kwargs: {'name': 'Ravi', 'age': 40}
