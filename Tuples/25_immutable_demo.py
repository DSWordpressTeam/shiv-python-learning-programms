# Program 25
# Tuples are Immutable

t = (1, 2, 3)
try:
    t[0] = 100
except TypeError as e:
    print("Cannot change:", e)

# Output:
# Cannot change: 'tuple' object does not support item assignment
