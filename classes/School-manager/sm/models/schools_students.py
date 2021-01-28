

def create_schools_students(cursor ,student_id ,school_id ,registration_date ,graduation_date ):
    try:
        query = "insert into schools_students (student_id ,school_id ,registration_date ,graduation_date) "
        query += f"values ({student_id},{school_id},{registration_date},{graduation_date})"
        cursor.execute(query)
        return True
    except Exception as e:
        print(e)
        return False

