from sm.models.schools import *

def create_school_controller(cursor,name):
    if not create_school(cursor,name):
        return None
    return "{} has been successfully created".format(name)

def get_schools_controller(cursor):
    return get_schools(cursor)