import csv
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="nupsg",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

def addStudent(name,stdid,hall,res,wing,wing2):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO students(`name`,`index_no`, `hall_of_affiliation`,`current_residence`,`wing`,`wing2`) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (name,stdid,hall,res,wing,wing2))
    finally:
        connection.commit()

with open('sample_students.csv', 'rt') as file:
    data = csv.reader(file)
    next(data)
    for i in data:
        addStudent(i[0],i[1],i[2],i[3],i[4],i[5])
    print("Done adding students!!")