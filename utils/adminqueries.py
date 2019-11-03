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



if __name__ == "__main__":
    addStudent("Dennis","PS/CSC/15/0004","KNH","SRC","asjda","asnda")