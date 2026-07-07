# Program 53
# Merge Two Frequency Dicts

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
result = a.copy()
for k, v in b.items():
    result[k] = result.get(k, 0) + v
print(result)

# Output:
# {'x': 1, 'y': 5, 'z': 4}
