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
            # if len(result) == 0:
            #     # NO user. GO ahead
            #     pass
            # else:
            #     # User already exits
            #     return result
    finally:
        return result

