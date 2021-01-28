from sm.models.students import *
from sm.models.careers import get_career_by_id
from sm.models.persons import *
from sm.models.schools_students import create_schools_students

def create_student_controller(cursor, first_name, last_name, birthday, career_id, school_id ,registration_date ,graduation_date):
    if get_career_by_id(cursor, career_id) is None:
        return None
    person_created = create_person(first_name, last_name, birthday)
    if not person_created:
        return None
    person = get_last_created_person(cursor)
    person_id = person[0]
    student_created = create_student(person_id, career_id)
    if not student_created:
        return None
    student = get_last_created_student(cursor)
    student_id = student[0]
    if not create_schools_students(cursor,student_id,school_id,registration_date,graduation_date):
        return None
    return "This student has been successfully created"


def get_students_controller(cursor):
    students = get_students(cursor)
    return students


def get_student_by_school_controller(cursor, school_id):
    students = get_students_by_school(cursor, school_id)
    return students


def update_student_controller(cursor, student_id, new_data):
    valid = True
    for k, v in new_data.items():
        if k == "" and v == "":
            valid = False
            break
    if valid:
        updated_student = update_student(cursor, student_id, new_data)
        if updated_student:
            return "This student has been updated successfully "
        return "An error occur during update"
    return "invalid parameters"


def get_student_by_id_controller(cursor, student_id):
    student = get_student_by_id(cursor, student_id)
    return student


def get_students_by_school_by_attendence_period_controller(cursor, school_id, start_date, end_date):
    students = get_student_by_school_by_attendence_period(cursor, school_id, start_date,end_date)
    return students


def get_graduated_students_by_promotion_controller(cursor, school_id, graduation_date):
    promotion = get_graduated_student_by_promotion(cursor, school_id, graduation_date)
    return promotion


def get_number_of_graduated_students_by_year_by_school_controller(cursor):
    graduated = get_number_of_graduated_students_by_year_by_school(cursor)
    return graduated


def get_max_graduated_student_controller(cursor):
    school = get_max_graduated_student_school(cursor)
    return school