def get_people(cursor):
    cursor.execute("select * from persons")
    return cursor.fetchall()

def create_person(cursor,first_name,last_name,birthday):
    try:
        request = "insert into persons (first_name,last_name,birthday) "
        request += f"values ({first_name},{last_name},{birthday})"
        cursor.execute(request)
        return True
    except Exception:
        return False


def get_last_created_person(cursor):
    cursor.execute(f"""select * from persons order by id
    desc limit 1""")
    return cursor.fetchone()


def update_person(cursor,id,new_data):
    request = "update persons set "
    items_length = len(new_data.values())
    item_count = 0
    for k,v in new_data.items():
        if item_count < items_length-1:
            request += f" {k} = {v}, "
        else:
            request += f" {k} = {v} "
        item_count += 1
    try:
        request += f" where id = {id};"
        cursor.execute(request)
        return True
    except Exception:
        return False

def delete_person(cursor,id):
    try:
        cursor.execute(f"delete from persons where id = {id}")
        return True
    except Exception:
        return False

def get_person_by_id(cursor,id):
    cursor.execute(f"select * from persons where id = {id}")
    return cursor.fetchone()
