# Program 27
# Sum of Digits

n = 1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)

# Output:
# Sum of digits: 10
