def check_name(name):
    return isinstance(name, str)

def get_school_name():
    valid_name = False
    name = ""
    while not valid_name :
        name = input("Enter the school name: ")
        if check_name(name):
            valid_name = True
            break
        print("Please enter a valid name")
    print(name)
    return name

def display_school_list(schools):
    for school in schools:
        print(school)