# Program 17
# Keyword-Only Arguments (using *)

def register(*, username, password):
    print("User:", username)
    print("Pass:", password)

register(username="admin", password="1234")

# Output:
# User: admin
# Pass: 1234
