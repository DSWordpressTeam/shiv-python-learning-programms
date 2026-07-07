# Program 31
# Key with Minimum Value

marks = {"math": 80, "sci": 90, "eng": 70}
print(min(marks, key=marks.get))

# Output:
# eng
