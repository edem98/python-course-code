from sm.models.students import get_student_by_id
from sm.models.courses import get_course_by_id
from sm.models.marks import *

def insert_mark_controller(cursor, student_id, course_id, mark):
    if get_student_by_id(cursor, student_id) is None:
        return None
    if get_course_by_id(cursor, course_id) is None:
        return None
    inserted = insert_mark(cursor, mark, course_id, student_id)
    if not inserted:
        return None
    return "This mark has been successfully insert"



def get_marks_controller(cursor):
    marks = get_marks(cursor)
    return marks


def get_marks_by_course_by_school_controller(cursor, course_id, student_id, school_id):
    marks = get_marks_by_course_by_school(cursor, course_id, student_id, school_id)
    return marks