# from cryptography.fernet import Fernet

master_pwd = input("What is the master passwrord? ")

# def write_key():
#   key = Fernet.generate_key()
#   with open("key.key", "wb") as key_file:
#     key_file.write(key)

# write_key()

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split(" - ")
            print("Account:", user, "| Password:", pwd)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{name} - {pwd}\n")

while True:
    mode = input("Do you want to add a new password or retrieve existing ones (add/view/quit)? ")
    if mode == "quit":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode. Please try again.")
        continue
