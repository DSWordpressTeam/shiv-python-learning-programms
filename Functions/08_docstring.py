# Program 8
# Function with Docstring

def area(radius):
    """Return the area of a circle for the given radius."""
    return 3.14 * radius * radius

print("Area:", area(5))
print("Doc:", area.__doc__)

# Output:
# Area: 78.5
# Doc: Return the area of a circle for the given radius.
