import getpass
import os

USERNAME = os.getenv("APP_USERNAME", "admin")
PASSWORD = os.getenv("APP_PASSWORD")


def login():
    """Check the supplied login credentials."""

    if not PASSWORD:
        print("Login is not configured. Please set APP_PASSWORD.")
        return

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    login()