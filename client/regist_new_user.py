from http_client import checking_username


def create_a_new_user():
    print("Welcome to new user creation:")
    username = input("Please enter a username: ")
    check_username = checking_username(username)
    if check_username == False:
        print("Username is taken. Please try a different name")
    else:
        return username

def create_a_new_password():
    password_1 = input("Please enter a password: ")
    while True:
        password_2 = input("Re-enter the password for verification: ")
        if password_1 == password_2:
            return password_1
        print("The passwords do not match please try again")




