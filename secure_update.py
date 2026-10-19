import getpass

USERNAME = "admin"

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username == USERNAME and password == "admin123":
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    login()