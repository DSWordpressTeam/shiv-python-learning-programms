# Program 30
# Full Argument Order (normal, *args, **kwargs)

def order(first, *args, **kwargs):
    print("First:", first)
    print("Args:", args)
    print("Kwargs:", kwargs)

order(1, 2, 3, x=10, y=20)

# Output:
# First: 1
# Args: (2, 3)
# Kwargs: {'x': 10, 'y': 20}
