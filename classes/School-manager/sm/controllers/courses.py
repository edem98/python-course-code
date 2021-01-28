from sm.models.courses import *
from sm.models.courses_careers import *


def create_course_controller(cursor,name,career_id,complexity,duration):
    if not create_course(cursor,name):
        return None
    course = get_last_course(cursor)
    course_id = course[0]
    if not create_courses_careers(cursor,career_id,course_id,complexity,duration):
        return None
    return "This course has been successfully created"