from client.http_client import request_last_reserve
from animal_search import (choose_search_type,
                           read_animal_id,
                           read_collar_code)
from output import show_last_reserve
from regist_new_user import (create_a_new_user,
                             create_a_new_password)
from http_client import regist_a_new_user

def main():
    search_choice = search_selection()
    if search_choice == 1:
        while True:
            search_type = choose_search_type()
            search_value = read_animal_id() if search_type == "id" else read_collar_code()
            result = request_last_reserve(search_type,search_value)
            data = result.json()
            show_last_reserve(data)
    if search_choice == 2:
        while True:
            username = create_a_new_user()
            password = create_a_new_password()
            regist_a_new_user(username,password)

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