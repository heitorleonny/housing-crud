import pymysql

def register_adress(latitude, longitude, region):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="ferraz2013",
        database="housing"
    )

    sql = f"""INSERT INTO latlongregion VALUES ({latitude}, {longitude}, '{region}')"""

    cursor = connection.cursor()
    cursor.execute(sql)  
    connection.commit()  

    cursor.close()
    connection.close()

register_adress(35.0228, -121.36, 'Camaragibe')