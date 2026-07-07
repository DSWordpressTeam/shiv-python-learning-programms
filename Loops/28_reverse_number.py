# Program 28
# Reverse a Number

n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed:", rev)

# Output:
# Reversed: 4321
