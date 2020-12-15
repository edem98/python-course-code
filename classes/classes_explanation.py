class Person:

    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return self.firstname+ " " +self.lastname

class Student(Person):

    def __init__(self,firstname,lastname,age,career):
        super().__init__(firstname,lastname,age)
        self.career = career

    def __str__(self):
        return "Student in {} : ".format(self.career.name) + super().__str__()

class Teacher(Person):

    def __init__(self,firstname,lastname,age):
        super().__init__(firstname,lastname,age)

    def __str__(self):
        return "Teacher: " + super().__str__()

class Career:

    def __init__(self,name):
        self.name = name
        self.courses = []

    def add_course(self,course):
        self.courses.append(course)

    def courses_list(self):
        return self.courses

    def search_course(self,name):
        for course in self.courses:
            if course.name == name:
                return course
        return None

    def __str__(self):
        return self.name

class Course:

    def __init__(self,name,duration,complexity):
        self.name = name
        self.duration = duration
        self.complexity = complexity

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def get_complexity(self):
        return self.complexity

    def __str__(self):
        return self.name



class Mark:

    def __init__(self,student,course,mark):
        self.student = student
        self.course = course
        self.mark = mark

    def __str__(self):
        return " {} {} have {} in {} : ".\
        format(self.student.firstname,self.student.lastname, self.mark,self.course.name )


class School:

    def __init__(self,name):
        self.students = []
        self.teachers = []
        self.name = name

    def add_student(self,student):
        self.students.append(student)

    def add_teacher(self,teacher):
        self.teachers.append(teacher)

    def __str__(self):
        return self.name



