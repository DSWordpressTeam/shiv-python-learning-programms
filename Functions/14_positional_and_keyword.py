# Program 14
# Mixing Positional and Keyword Arguments

def order(item, qty, price):
    print(qty, item, "cost", qty * price)

order("Pens", 5, price=10)

# Output:
# 5 Pens cost 50
