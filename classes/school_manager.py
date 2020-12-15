from classes_explanation import Course, Career, Student, School

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

course = bigdata.search_course("learn python")
if course:
    print("I found the course: {} and his duration is {} hours".format(course.name,course.duration))
else:
    print("This course doesn't exist in this career")


eric = Student("Eric","Tsogbe",23,software)
serge = Student("serge","kossi",22,bigdata)

print(eric)

x = int(5)
tamtam = School("TamTam Digital School and Community Center")
print(tamtam)
