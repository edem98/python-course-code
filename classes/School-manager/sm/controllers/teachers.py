from sm.models.teachers import *
from sm.models.careers import get_career_by_id
from sm.models.persons import *
from sm.models.schools_teachers import create_schools_teachers



def create_teacher_controller(cursor, first_name, last_name, birthday, career_id,school_id ,start_date ,end_date):
    if get_career_by_id(cursor, career_id) is None:
        return None
    person_created = create_person(first_name, last_name, birthday)
    if not person_created:
        return None
    person = get_last_created_person(cursor)
    person_id = person[0]
    teacher_created = create_teacher(person_id, career_id)
    if not teacher_created:
        return None
    teacher = get_last_created_teacher(cursor)
    teacher_id = teacher[0]
    if not create_schools_teachers(cursor,teacher_id,school_id,start_date,end_date):
        return None
    return "This teacher has been successfully created"



def get_teachers_controller(cursor):
    teachers = get_teachers(cursor)
    return teachers


def get_teachers_by_school_controller(cursor, school_id):
    teachers = get_teacher_by_school(cursor, school_id)
    return teachers


def update_teacher_controller(cursor, teacher_id, new_data):
    valid = True
    for k, v in new_data.items():
        if k == "" and v == "":
            valid = False
            break
    if valid:
        updated_teacher = update_teacher(cursor, teacher_id, new_data)
        if updated_teacher:
            return "This teacher has been updated successfully "
        return "An error occur during update"
    return "invalid parameters"


def get_teacher_by_id_controller(cursor, teacher_id):
    teacher = get_teacher_by_id(cursor, teacher_id)
    return teacher


def get_teachers_by_school_by_career_controller(cursor, career_id, school_id):
    teachers = get_teachers_by_school_by_career(cursor, career_id, school_id)
    return teachers