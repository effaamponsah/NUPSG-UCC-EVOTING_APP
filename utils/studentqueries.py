import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="nupsg",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

def studentLogin(indexNumber):
    try:
        with connection.cursor() as cursor:
            query1 = "SELECT * FROM `students` WHERE `index_no`=%s"
            cursor.execute(query1, (indexNumber))
            result = cursor.fetchone()
    finally:
        return result

