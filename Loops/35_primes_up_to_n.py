# Program 35
# Print Primes up to N

for num in range(2, 20):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")

# Output:
# 2 3 5 7 11 13 17 19 
