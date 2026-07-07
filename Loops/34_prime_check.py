# Program 34
# Check Prime Number

n = 13
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")

# Output:
# Prime
