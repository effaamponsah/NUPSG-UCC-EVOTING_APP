# This counter file is a function that take in the position
# and name of the voted for aspirant and increments 
# it by one

import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="nupsg",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


def increment(position,name):
    try:
        with connection.cursor() as cursor:
            query2 = "UPDATE "+position+" SET `votes`=votes+%s WHERE `name`=%s"
            cursor.execute(query2, (1, name))
            result = cursor.fetchone()
           
    finally:
        connection.commit()


def viewResults(table):
    try:
        with connection.cursor() as cursor:
            query1 = "SELECT `name`,`votes` FROM "+table
            cursor.execute(query1)
            result = cursor.fetchall()
           
    finally:
        return result
    

viewResults('president')