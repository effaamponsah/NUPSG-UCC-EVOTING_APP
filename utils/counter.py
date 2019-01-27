# This counter file is a function that take in the position
# and name of the voted for aspirant and increments 
# it by one

import sqlite3 as sql


def increment(position,name):
    # dbConnect = sql.connect('polls.db')
    # coursor = dbConnect.cursor()
    # coursor.execute("UPDATE "+position+" SET votes =votes+?  WHERE name= ?", (1, name))
    # dbConnect.commit()
    # x = 'added'
    # print (x)
    try:
        with sql.connect('polls.db') as dbConnect:
            coursor = dbConnect.cursor()
            coursor.execute("UPDATE "+position+" SET votes =votes+?  WHERE name= ?", (1, name))
            dbConnect.commit()
            message = 'Success'
    except:
        dbConnect.rollback()
        message = 'Error Occured'
    finally:
        dbConnect.close()
        print(message)