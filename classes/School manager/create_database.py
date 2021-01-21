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

# create tables
cursor.execute("""

    create table persons (
        id int auto_increment primary key,
        first_name varchar(45) not null,
        last_name varchar(45) not null,
        birthday date not null
    );
    
    create table courses (
        id int auto_increment primary key,
        name varchar(45) not null
    );
    
    create tables careers (
        id int auto_increment primary key,
        name varchar(45) not null
    );
    
    create tables school (
        id int auto_increment primary key,
        name varchar(45) not null
    );
    
    create tables teachers (
        id int auto_increment primary key,
        person_id int not null,
        career_id int not null,
        foreign key person_id reference persons(id),
        foreign key career_id reference careers(id)
    );
    
    create tables students (
        id int auto_increment primary key,
        person_id int not null,
        career_id int not null,
        foreign key person_id reference persons(id),
        foreign key career_id reference careers(id)
    );
    
    create tables marks (
        id int auto_increment primary key,
        mark int not null,
        course_id int not null,
        student_id int not null,
        foreign key course_id reference courses(id),
        foreign key student_id reference students(id)
    );
    
    create tables courses_careers (
        course_id int not null,
        career_id int not null,
        complexity int not null,
        duration int not null,
        constraint primary key(course_id,career_id),
        foreign key course_id reference courses(id),
        foreign key student_id reference students(id)
    );
    
    create tables schools_students (
        student_id int not null,
        school_id int not null,
        registration_date date not null,
        graduation_date date,
        constraint primary key(student_id,school_id),
        foreign key school_id reference schools(id),
        foreign key student_id reference students(id)
    );
    
    create tables schools_teachers (
        student_id int not null,
        school_id int not null,
        start_date date not null,
        end_date date not null,
        constraint primary key(student_id,school_id),
        foreign key school_id reference schools(id),
        foreign key student_id reference students(id)
    );
    
""",multi=True)

