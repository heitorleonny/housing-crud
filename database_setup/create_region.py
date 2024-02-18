import pymysql

def create_region(region,state):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="pph1112003",
        database="housing"
    )

    sql = f"""INSERT INTO regionstate (region,state)
             VALUES ( '{region}', '{state}')"""

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit() 

    cursor.close()
    connection.close()
