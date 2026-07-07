# Program 45
# Remove Item by Value

d = {"a": 1, "b": 2, "c": 1}
d = {k: v for k, v in d.items() if v != 1}
print(d)

# Output:
# {'b': 2}
