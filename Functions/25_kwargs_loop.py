# Program 25
# Looping Over **kwargs

def details(**info):
    for key, value in info.items():
        print(key, ":", value)

details(name="Sara", city="Delhi", age=30)

# Output:
# name : Sara
# city : Delhi
# age : 30
