# Program 20
# Argument Unpacking with * and **

def info(name, age):
    print(name, "-", age)

data_list = ["Kiran", 22]
data_dict = {"name": "Meena", "age": 28}

info(*data_list)
info(**data_dict)

# Output:
# Kiran - 22
# Meena - 28
