import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="nupsg",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

postitions = ['atl_hall','adehye_hall','amamoma','apewosika','casford_hall','knh_hall','kwaprow','oguaa_hall', 'src_hall','superannuation','valco_hall', 'chapel_steward','choir_president', 'evang_cord', 'organizing_sec', 'prayer_sec', 'president', 'sch_cord', 'secretary', 'welfare_chair']

def createstudents():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE `students` ( `studentid` INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT NULL , `index_no` TEXT NOT NULL , `hall_of_affiliation` TEXT NOT NULL , `current_residence` TEXT NOT NULL , `wing` TEXT NULL , `wing2` TEXT NULL , PRIMARY KEY (`studentid`)) ENGINE = MyISAM"
                )
    finally:
        connection.commit()




def createpostitions():
    try:
        with connection.cursor() as cursor:
            for i in postitions:
                cursor.execute(
"CREATE TABLE "+i+" ( positionid INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT NULL , `votes` INT NOT NULL DEFAULT '0' , PRIMARY KEY (`positionid`)) ENGINE = MyISAM"
                )
    finally:
        connection.commit()


def createTotalsTable():
    return True

createstudents()
createpostitions()