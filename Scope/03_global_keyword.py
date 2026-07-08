# Program 3
# global Keyword

count = 0

def increment():
    global count
    count += 1

increment()
increment()
print("Count:", count)

# Output:
# Count: 2
