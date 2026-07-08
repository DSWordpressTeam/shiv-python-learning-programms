# Program 6
# Timer Decorator

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", round(end - start, 2), "seconds")
        return result
    return wrapper

@timer
def slow():
    time.sleep(1)
    print("Done")

slow()

# Output:
# Done
# Time taken: 1.0 seconds
