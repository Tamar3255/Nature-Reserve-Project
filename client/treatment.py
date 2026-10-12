


def create_treatment():
    date = "default"
    animal_id = int(input("please enter 'animal id': "))
    ranger_id = int(input("please enter 'ranger id': "))
    reserve_id = int(input("please enter 'reserve id': "))
    while True:
        outcome = input("Please enter the current medical condition: ")
        if outcome in ["healthy", "treated", "relocated"]:
            break
        else:
            print("value error. please try again: ")
    treatment = {"date": date, "animal id": animal_id, "ranger id": ranger_id, "reserve id": reserve_id,"outcome": outcome}
    return treatment