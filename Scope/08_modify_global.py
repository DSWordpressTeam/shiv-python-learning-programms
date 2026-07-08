# Program 8
# Modifying a Global Variable

balance = 1000

def deposit(amount):
    global balance
    balance += amount

deposit(500)
print("Balance:", balance)

# Output:
# Balance: 1500
