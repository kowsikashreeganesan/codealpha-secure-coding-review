USERNAME = "admin"
PASSWORD = "admin123"

def login(username, password):
    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
    else:
        print("Invalid username or password.")

login("admin", "admin123")