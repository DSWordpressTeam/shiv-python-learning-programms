# Program 36
# Filter Dictionary

marks = {"math": 80, "sci": 40, "eng": 90}
passed = {k: v for k, v in marks.items() if v >= 50}
print(passed)

# Output:
# {'math': 80, 'eng': 90}
