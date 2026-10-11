

def choose_search_type():
    while True:
        print("for search by 'id' enter 1")
        print("for search by 'collar code' enter 2")
        choice = input("please enter your choice: ")
        if int(choice) == 1:
            return "id"
        if int(choice) == 2:
            return "collar code"
        print("try again")

def read_animal_id():
    while True:
        id_value = input("please enter animal id: ")
        if id_value.isdigit() and int(id_value) > 0:
          return int(id_value)
        print("Please enter a positive integer: ")


def read_collar_code():
    while True:
        collar_code_value = input("please enter collar code id: ")
        if collar_code_value.startswith("col"):
            return collar_code_value
        print("Please try again")




