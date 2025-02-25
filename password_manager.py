master_pwd = input("What is the master passwrord? ")

def view():
    pass

view()

def add():
    pass

while True:
    mode = input("Do you want to add a new password or retrieve existing ones (add/view/quit)? ")
    if mode == "quit":
        break
    elif mode == "add":
        pass
    elif mode == "view":
        pass
    else:
        mode = input("Invalid mode. Do you want to add a new password or retrieve existing ones (add/view)? ")
        continue

# if mode == "add":
#     new_pwd = input("What is the new password? ")
#     with open("passwords.txt", "a") as f:
#         f.write(f"{pwd} {new_pwd}\n")
# elif mode == "view":
#     with open("passwords.txt", "r") as f:
#         for line in f:
#             master_pwd, pwd = line.split()
#             if master_pwd == pwd:
#                 print(pwd)
# else:
#     print("Invalid mode")



