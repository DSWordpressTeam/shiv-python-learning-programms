# Program 4
# Local vs Global (Same Name)

x = 100

def show():
    x = 5
    print("Local x:", x)

show()
print("Global x:", x)

# Output:
# Local x: 5
# Global x: 100
