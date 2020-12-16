from classes_explanation import Course, Career, Student, School, Teacher

# My courses
python = Course("learn python",10,1)
etl = Course("Learn ETL",10,1)
sql = Course("Learn SQL",10,1)
mongodb = Course("Learn MongoDB",10,1)
javascript = Course("Javascript",10,1)
html_css = Course("HTML and CSS3",10,1)
# first career
bigdata = Career("Big Data and Data Analysis")
bigdata.add_course(python)
bigdata.add_course(etl)
bigdata.add_course(sql)
bigdata.add_course(mongodb)
# second career
software = Career("Software development and User Interfaces")
software.add_course(python)
software.add_course(html_css)
software.add_course(javascript)
software.add_course(sql)

# school
tamtam = School("TamTam Digital School")
# students
eliram = Student("eliram", "gbogbo", 30, bigdata)
prosper = Student("prosper", "alikizang", 24, bigdata)
# teachers
serge = Teacher("serge", "kossi", 18, bigdata)
eric = Teacher("eric", "tsogbe", 18, software)
#Assign
tamtam.add_student(eliram)
tamtam.add_student(prosper)
tamtam.add_teacher(serge)
tamtam.add_teacher(eric)

age = 30
students = tamtam.get_student_by_age(age)
for student in students:
    print(student.firstname, "is {} years old".format(age))


# # students list
# l = tamtam.get_students()
# for i in l:
#     print(i)
#
# r = tamtam.get_teachers()
# for i in r:
#     print(i)





