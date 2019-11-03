import pymysql
import json
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="nupsg",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


'''
The example below shows how you should input the names of the candidates.
Fill in the boxes with the names against each position

Example:
adehye =[ "Barbara", "Hannah" ]

The above indicates that the candidates are Barbara and Hannah. You can enter as many 
asiprants as possible.

THAT IS THE ONLY THING TO CHANGE IN THIS FILE!!!!

It should be run once. So ensure all details are correct.
And be mindful of spaces. Computers are dump :)

'''
atl=[]
adehye = []
amamoma = []
apewosika=[]
casford=[]
knh=[]
kwaprow=[]
oguaa=[]
src=[]
superannuation=[]
valco=[] 
chapelSteward=[]
choirPresident=[]
evangCord=[]
organizingSec=[]
prayerSec=[]
president=[]
schCord=[]
secretary=[]
welfare=[]

def fillPositions():
    data = {}
    try:
        with connection.cursor() as cursor:
            # Dumps it into the data.json file
            data['President'] = {}
            data['President']['role'] = "President"
            data['President']['name'] =[]
            data['President']['images'] =[]
            
            data['Secretary'] = {}
            data['Secretary']['role'] = "Secretary"
            data['Secretary']['name'] =[]
            data['Secretary']['images'] =[]
            
            data['Welfare-Chairperson'] = {}
            data['Welfare-Chairperson']['role'] = "Welfare-Chairperson"
            data['Welfare-Chairperson']['name'] =[]
            data['Welfare-Chairperson']['images'] =[]
            
            data['Adehye-HALL'] = {}
            data['Adehye-HALL']['role'] = "Adehye-HALL REP"
            data['Adehye-HALL']['name'] =[]
            data['Adehye-HALL']['images'] =[]
            
            data['Amamoma'] = {}
            data['Amamoma']['role'] = "Amamoma REP"
            data['Amamoma']['name'] =[]
            data['Amamoma']['images'] =[]
            
            data['Apewosika'] = {}
            data['Apewosika']['role'] = "Apewosika REP"
            data['Apewosika']['name'] =[]
            data['Apewosika']['images'] =[]
            
            data['Casford-HALL'] = {}
            data['Casford-HALL']['role'] = "Casford-HALL REP"
            data['Casford-HALL']['name'] =[]
            data['Casford-HALL']['images'] =[]

            data['KNH-HALL'] = {}
            data['KNH-HALL']['role'] = "KNH-HALL REP"
            data['KNH-HALL']['name'] =[]
            data['KNH-HALL']['images'] =[]

            data['Kwaprow'] = {}
            data['Kwaprow']['role'] = "Kwaprow REP"
            data['Kwaprow']['name'] =[]
            data['Kwaprow']['images'] =[]

            data['Oguaa-HALL'] = {}
            data['Oguaa-HALL']['role'] = "Oguaa-HALL REP"
            data['Oguaa-HALL']['name'] =[]
            data['Oguaa-HALL']['images'] =[]

            data['SRC-HALL'] = {}
            data['SRC-HALL']['role'] = "SRC-HALL REP"
            data['SRC-HALL']['name'] =[]
            data['SRC-HALL']['images'] =[]

            data['Superannuation-Hostel'] = {}
            data['Superannuation-Hostel']['role'] = "Superannuation-Hall REP"
            data['Superannuation-Hostel']['name'] =[]
            data['Superannuation-Hostel']['images'] =[]

            data['Valco-HALL'] = {}
            data['Valco-HALL']['role'] = "Valco-HALL REP"
            data['Valco-HALL']['name'] =[]
            data['Valco-HALL']['images'] =[]

            data['Chapel-Steward'] = {}
            data['Chapel-Steward']['role'] = "Chapel-Steward"
            data['Chapel-Steward']['name'] =[]
            data['Chapel-Steward']['images'] =[]

            data['Choir-President'] = {}
            data['Choir-President']['role'] = "Choir-President"
            data['Choir-President']['name'] =[]
            data['Choir-President']['images'] =[]

            data['Evangelism-Coordinator'] = {}
            data['Evangelism-Coordinator']['role'] = "Evangelism-Coordinator"
            data['Evangelism-Coordinator']['name'] =[]
            data['Evangelism-Coordinator']['images'] =[]

            data['Organizing-Secretary'] = {}
            data['Organizing-Secretary']['role'] = "Organizing-Secretary"
            data['Organizing-Secretary']['name'] =[]
            data['Organizing-Secretary']['images'] =[]

            data['Prayer-Secretary'] = {}
            data['Prayer-Secretary']['role'] = "Prayer-Secretary"
            data['Prayer-Secretary']['name'] =[]
            data['Prayer-Secretary']['images'] =[]

            data['Schools Coordinator'] = {}
            data['Schools Coordinator']['role'] = "School's Coordinator"
            data['Schools Coordinator']['name'] =[]
            data['Schools Coordinator']['images'] =[]

            data['ATL-HALL'] = {}
            data['ATL-HALL']['role'] = "ATL-HALL REP"
            data['ATL-HALL']['name'] =[]
            data['ATL-HALL']['images'] =[]


            for i in secretary:
                sql = "INSERT INTO secretary(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Secretary']['name'].append(i)
                
            for b in welfare:
                sql = "INSERT INTO welfare_chair(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(b)
                    )
                data['Welfare-Chairperson']['name'].append(b)
            
            for i in adehye:
                sql = "INSERT INTO adehye_hall(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Adehye-HALL']['name'].append(i)
                   
            for i in amamoma:
                sql = "INSERT INTO amamoma(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Amamoma']['name'].append(i)
            
            for i in apewosika:
                sql = "INSERT INTO apewosika(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Apewosika']['name'].append(i)

            for i in casford:
                sql = "INSERT INTO casford_hall(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Casford-HALL']['name'].append(i)

            for i in knh:
                sql = "INSERT INTO knh_hall(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['KNH-HALL']['name'].append(i)

            for i in kwaprow:
                sql = "INSERT INTO kwaprow(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Kwaprow']['name'].append(i)
            
            for i in oguaa:
                sql = "INSERT INTO oguaa_hall(`name`) VALUES(%s) "
                cursor.execute(sql,(i))
                data['Oguaa-HALL']['name'].append(i)
            
            for i in src:
                sql = "INSERT INTO src_hall(`name`) VALUES(%s) "
                cursor.execute(sql,(i))
                data['SRC-HALL']['name'].append(i)

            for i in superannuation:
                sql = "INSERT INTO superannuation(`name`) VALUES(%s) "
                cursor.execute(sql,(i))
                data['Superannuation-Hostel']['name'].append(i)
            
            for i in valco:
                sql = "INSERT INTO valco_hall(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Valco-HALL']['name'].append(i)
            
            for i in chapelSteward:
                sql = "INSERT INTO chapel_steward(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Chapel-Steward']['name'].append(i)

            for i in choirPresident:
                sql = "INSERT INTO choir_president(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Choir-President']['name'].append(i)
            
            for i in evangCord:
                sql = "INSERT INTO evang_cord(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Evangelism-Coordinator']['name'].append(i)
            
            for i in organizingSec:
                sql = "INSERT INTO organizing_sec(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Organizing-Secretary']['name'].append(i)
            
            for i in prayerSec:
                sql = "INSERT INTO prayer_sec(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Prayer-Secretary']['name'].append(i)
            
            for i in president:
                sql = "INSERT INTO president(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['President']['name'].append(i)
                
            for i in schCord:
                sql = "INSERT INTO sch_cord(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['Schools Coordinator']['name'].append(i)

            for i in atl:
                sql = "INSERT INTO atl_hall(`name`) VALUES(%s) "
                cursor.execute(
                    sql,(i)
                    )
                data['ATL-HALL']['name'].append(i)
                

    finally:
        with open('../seed/data.json','w') as out:
            json.dump(data,out)
        connection.commit()                

            


fillPositions()