# Program 48
# GCD of Two Numbers

a, b = 48, 18
while b:
    a, b = b, a % b
print("GCD:", a)

# Output:
# GCD: 6
