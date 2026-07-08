# Program 10
# Each Function Has Its Own Scope

def func_a():
    x = "A"
    print("func_a:", x)

def func_b():
    x = "B"
    print("func_b:", x)

func_a()
func_b()

# Output:
# func_a: A
# func_b: B
