import pymysql

def create_region(region,state):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="ferraz2013",
        database="housing"
    )

    sql = f"""INSERT INTO regionstate (region,state)
             VALUES ( '{region}', '{state}')"""

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit() 

    cursor.close()
    connection.close()

create_region('Camaragibe', 'Pernambuco')