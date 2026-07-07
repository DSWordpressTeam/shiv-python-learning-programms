# Program 39
# Loop Nested Dictionary

students = {"s1": {"name": "Shiv"}, "s2": {"name": "Ram"}}
for sid, info in students.items():
    print(sid, "->", info["name"])

# Output:
# s1 -> Shiv
# s2 -> Ram
