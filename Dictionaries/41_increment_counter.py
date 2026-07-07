# Program 41
# Increment a Counter

counter = {}
for x in [1, 2, 1, 3, 1]:
    counter[x] = counter.get(x, 0) + 1
print(counter)

# Output:
# {1: 3, 2: 1, 3: 1}
