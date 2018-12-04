import sqlite3

conn = sqlite3.connect("my.db")
c = conn.cursor()

c.execute("CREATE TABLE if not exists course (id INTEGER PRIMARY KEY ASC AUTOINCREMENT UNIQUE,name varchar)")
for i in range(int(input("quantity of courses: "))):
    s = input('name course: ')
    c.execute(f"INSERT INTO course (name) VALUES ('{s}')")
    conn.commit()

c.execute('SELECT * FROM course')
result = c.fetchall()
courses = []
for item in result:
    print(item)
    courses.append(item)

c.execute("CREATE TABLE if not exists students (id INTEGER PRIMARY KEY ASC AUTOINCREMENT UNIQUE,name varchar)")
for i in range(int(input("quantity of students: "))):
    s = input('name course: ')
    c.execute(f"INSERT INTO students (name) VALUES ('{s}')")
    conn.commit()

c.execute('SELECT * FROM students')
result = c.fetchall()
students = []
for item in result:
    print(item)
    students.append(item)

#c.execute("CREATE TABLE if not exists multiple (id INTEGER PRIMARY KEY ASC AUTOINCREMENT UNIQUE,id_student varchar,id_course varchar)")

c.execute('SELECT * FROM multiple')
result = c.fetchall()
m = []
print("\nстудент: факультет")
for item in result:
    #print(item)
    m.append(item)
    idstudent = item[1]
    idcourse = item[2]
    namestud = ""
    for i in range(len(students)):
        if students[i][0] == idstudent:
            namestud = students[i][1]
    namecour = ""
    for i in range(len(courses)):
        if courses[i][0] == idcourse:
            namecour = courses[i][1]
    print(namestud + ": " + namecour)
    #select name.table1 from table1,table3 where id.table1=idt3.table3 group by name

print("\nили так\n")
c.execute("SELECT students.name,course.name FROM students,multiple,course WHERE students.id=multiple.id_student AND course.id=multiple.id_course")
res = c.fetchall()
for item in res:
    print(item[0] + ": " + item[1])

conn.close()