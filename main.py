import os.path

print(
    """
█▀▀ █▀█ █▄░█ █▀ █▀█ █░░ █▀▀   █▀█ █▀
█▄▄ █▄█ █░▀█ ▄█ █▄█ █▄▄ ██▄   █▄█ ▄█
          by @nathanielrz
"""
)
username = input("Enter your username: ")
path = "./users/" + username + ".txt"
if username:
    password = input("Enter your password: ")
    user = os.path.isfile(path)
    if user:
        if password == open(path, "r").read():
            print("Logged in")
        else:
            print("Password inccorrect")
    else:
        create = input(
            "User does not exists, would you like to create this account? (Y/N): "
        )
        if create == "Y":
            file = open(path, "a")
            file.write(password)
        else:
            print("Cancelled!")
