# Program 10
# Lambda Returning a Lambda

multiplier = lambda n: lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))

# Output:
# 20
# 30
