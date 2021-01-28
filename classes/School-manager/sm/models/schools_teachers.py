
def create_schools_teachers(cursor ,teacher_id ,school_id ,start_date ,end_date ):
    try:
        query = "insert into schools_teachers (teacher_id ,school_id ,start_date ,end_date) "
        query += f"values ({teacher_id},{school_id},{start_date},{end_date})"
        cursor.execute(query)
        return True
    except Exception as e:
        print(e)
        return False

