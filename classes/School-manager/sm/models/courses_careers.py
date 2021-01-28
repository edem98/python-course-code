

def create_courses_careers(cursor,course_id,career_id,complexity,duration):
    try:
        query = "insert into courses_careers (course_id,career_id,complexity,duration) "
        query += f"values ({course_id},{career_id},{complexity},{duration})"
        cursor.execute(query)
        return True
    except Exception as e:
        print(e)
        return False

