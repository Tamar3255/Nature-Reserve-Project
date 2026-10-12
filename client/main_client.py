from client.http_client import request_last_reserve
from animal_search import (choose_search_type,
                           read_animal_id,
                           read_collar_code)
from output import show_last_reserve
from regist_new_user import (create_a_new_user,
                             create_a_new_password)
from http_client import regist_a_new_user
from treatment import create_treatment
from http_client import access_approval
from http_client import update_treatment




def main():
    while True:
        search_choice = search_selection()
        if search_choice == 1:
            search_type = choose_search_type()
            if search_type == "back":
                continue
            search_value = read_animal_id() if search_type == "id" else read_collar_code()
            result = request_last_reserve(search_type,search_value)
            data = result.json()
            show_last_reserve(data)
        if search_choice == 2:
            username = create_a_new_user()
            password = create_a_new_password()
            r = regist_a_new_user(username,password)
            print(r)
        if search_choice == 3:
            print("Hello welcome to the treatment registration system. ")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            access_approvd = access_approval(username,password)
            if access_approvd == "exists":
                treatment = create_treatment()
                update_treatment(treatment)
            else:
                print("The entered username or password is incorrect please try again")










def search_selection():
    print("1. Search Animal Last Seen Reserve (Search by ID / Collar Code)"
          "\n2. Register New User"
          "\n3. Add New Treatment (Authenticated)"
          "\n4. Ranger Investigation (Authenticated)"
          "\n5. Exit")
    search_choice = int(input(f"Please select an option (1-5): "))
    return search_choice



if __name__ == "__main__":
    main()