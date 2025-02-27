master_pwd = input("What is the master passwrord? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f:
            print(line)

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
        mode = input("Invalid mode. Do you want to add a new password or retrieve existing ones (add/view)? ")
        continue
