import mysql.connector as conn

db = conn.connect(host="127.0.0.1",user="devuser",password="sergedem",
                  port=3306,auth_plugin='mysql_native_password')

cursor = db.cursor()

# drop database if exists
cursor.execute("""
    drop database school;
""")

# create database named school
cursor.execute("""
    create database school;
""")

# use database school
cursor.execute("""
    use school;
""")

cursor.execute("""

    create table persons (
        id int auto_increment primary key,
        first_name varchar(45) not null,
        last_name varchar(45) not null,
        birthday date not null
    );
    
""");

cursor.execute("""

    create table courses (
        id int auto_increment primary key,
        name varchar(45) not null
    );

""");

cursor.execute("""

    create table careers (
        id int auto_increment primary key,
        name varchar(45) not null
    );
    
""");

cursor.execute("""

    create table schools (
        id int auto_increment primary key,
        name  varchar(45) not null
    );
    
""");

cursor.execute("""

    create table teachers (
        id int auto_increment primary key,
        person_id int not null,
        career_id int not null,
        foreign key (person_id) references persons(id),
        foreign key (career_id) references careers(id)
);

""");

cursor.execute("""

create table students (
        id int auto_increment primary key,
        person_id int not null,
        career_id int not null,
        foreign key (person_id) references persons(id),
        foreign key (career_id) references careers(id)
    );
        
""");

cursor.execute("""
    
    create table marks (
        id int auto_increment primary key,
        mark int not null,
        course_id int not null,
        student_id int not null,
        foreign key (course_id) references courses(id),
        foreign key (student_id) references students(id)
    );

""");

cursor.execute("""

    create table courses_careers (
        course_id int not null,
        career_id int not null,
        complexity int not null,
        duration int not null,
		student_id int not null,
        constraint primary key(course_id,career_id),
        foreign key (course_id) references courses(id),
        foreign key (student_id) references students(id)
    );
    
""");

cursor.execute("""
    
    create table schools_students (
        student_id int not null,
        school_id int not null,
        registration_date date not null,
        graduation_date date,
        constraint primary key(student_id,school_id),
        foreign key (school_id) references schools(id),
        foreign key (student_id) references students(id)
    );
    
""");

cursor.execute("""
    
    create table schools_teachers (
        teacher_id int not null,
        school_id int not null,
        start_date date not null,
        end_date date not null,
        constraint primary key(teacher_id,school_id),
        foreign key (school_id) references schools(id),
        foreign key (teacher_id) references teachers(id)
    );

""")

cursor.execute("show tables;")
print(cursor.fetchall())

db.close()