from .schools import get_school_name, display_school_list
from sm.controllers.schools import *

def welcome():
    print("-------------------------------------------------------------")
    print("--------------    Welcome in School Manager    --------------")
    print("-------------------------------------------------------------")

def goodbye():
    print("-------------------------------------------")
    print("--------------    Goodbye    --------------")
    print("-------------------------------------------")

def show_actions():
    print(" Which action do you what to perform ?")
    print("")
    print("1- Add a new school ")
    print("2- Add a new career ")
    print("3- Add a new course ")
    print("4- Add a new student ")
    print("5- Add a new teacher ")
    print("6- Get schools list ")

    choice_correct = False
    while not choice_correct:
        choice = int(input(" Enter your choice (1 to 6): "))
        if 0 < choice < 7 :
            choice_correct = True
            break
        print("Please make a valid choice")

    return choice

def main_view(cursor):
    welcome()
    answer = "y"
    while answer in "yY":
        action = show_actions()
        if action == 1:
            school_name = get_school_name()
            response = create_school_controller(cursor,school_name)
            print(response)
        if action == 6:
            display_school_list(get_schools_controller(cursor))
        print("")
        answer = input("Do you want to continue? (y/n):  ")
    goodbye()



