# Program 47
# Collatz Sequence

n = 6
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(1)

# Output:
# 6 3 10 5 16 8 4 2 1
