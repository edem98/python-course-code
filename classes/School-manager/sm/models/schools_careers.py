
def create_schools_careers(cursor ,career_id ,school_id ,start_date ,end_date = None ):
    try:
        query = "insert into schools_careers (career_id ,school_id ,start_date ,end_date) "
        if end_date is None:
            query += f"values ({career_id},{school_id},'{start_date}',null)"
        else:
            query += f"values ({career_id},{school_id},'{start_date}','{end_date}')"
        cursor.execute(query)
        return True
    except Exception as e:
        print(e)
        return False