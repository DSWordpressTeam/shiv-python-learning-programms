# Program 26
# Count Digits of a Number

n = 45678
count = 0
while n > 0:
    n //= 10
    count += 1
print("Digits:", count)

# Output:
# Digits: 5
