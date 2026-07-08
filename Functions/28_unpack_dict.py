# Program 28
# Unpacking a Dictionary into **kwargs

def person(name, age):
    print(name, "is", age)

data = {"name": "Neha", "age": 22}
person(**data)

# Output:
# Neha is 22
