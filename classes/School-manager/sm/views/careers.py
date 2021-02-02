from datetime import datetime

def get_career():
    valid = False
    while not valid:
        name = input("Enter the career name: ")
        school_id = int(input("Enter the school id: "))
        if isinstance(name,str) and isinstance(school_id,int):
            return name, school_id, datetime.now().strftime("%Y-%m-%d")

def show_careers(careers):
    for career in careers:
        print(career)