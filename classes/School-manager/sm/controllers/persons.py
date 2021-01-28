from sm.models.persons import *


def get_people_controller(cursor):
    people = get_people(cursor)
    return people


def create_person_controller(cursor, first_name, last_name, birthday):
    if first_name != "" and last_name != "" and birthday != "":
        created_person = create_person(cursor, first_name, last_name, birthday)
        if created_person:
            return "This person has been added successfully"
        return "An error occur during creation"
    return "Invalid parameters"


def update_person_controller(cursor, id, new_data):
    valid = True
    for k, v in new_data.items():
        if k == "" or v == "":
            valid = False
            break
    if valid:
        updated_person = update_person(cursor, id, new_data)
        if updated_person:
            return "This person has been updated successfully "
        return "An error occur during update"
    return "Invalid parameters"


def delete_person_controller(cursor, id):
    remove = delete_person(cursor, id)
    if remove:
        return "This person has been deleted successfully"
    return "An error occur during deletion"


def get_person_by_id_controller(cursor, id):
    person = get_person_by_id(cursor, id)
    return person