from sm.models.schools_careers import *
from sm.models.careers import *
from sm.models.schools import get_school_by_id

def create_career_controller(cursor, name, school_id, start_date, end_date = None):
    if not create_career(cursor,name):
        return None
    career = get_last_careers(cursor)
    career_id = career[0]
    if end_date is None:
        school = create_schools_careers(cursor, career_id, school_id, start_date)
    else:
        school = create_schools_careers(cursor, career_id, school_id, start_date, end_date)
    if school:
        return "This career has been successfully created"
    return None



def get_careers_controller(cursor):
    careers = get_career(cursor)
    return careers


def get_career_by_school_controller(cursor, school_id):
    if get_school_by_id(cursor, school_id) is None:
        return None
    career = get_career_by_school(cursor, school_id)
    return career
