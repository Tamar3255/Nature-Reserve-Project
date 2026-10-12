
def show_last_reserve(result):
    print(result)
    print("===Results===")
    print(f"Animal ID: {result["animal_id"]}")
    print(f"Collar code: {result["collar_code"]}")
    print(f"Species: {result["species"]} ({result["nickname"]})")
    print(f"Last seen reserve: {result["reserve_name"]}")
    print(f"Region: {result["region"]}")
    print(f"Description: {result["description"]}")
    print(f"!!!!Done!!!!")