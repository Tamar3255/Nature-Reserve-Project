

def create_a_new_user():
    print("Welcome to new user creation:")
    while True:
        username = input("Please enter a username: ")
        if username == " ":
            print("username can't be empty")
        else:
            return username

def create_a_new_password():
    password_1 = input("Please enter a password: ")
    while True:
        if password_1 == " ":
            print("password can't be empty")
        password_2 = input("Re-enter the password for verification: ")
        if password_1 == password_2:
            return password_1
        print("The passwords do not match please try again")




