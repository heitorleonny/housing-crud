import pymysql

def register_adress(latitude, longitude, region):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="ferraz2013",
        database="housing"
    )

    try:
        sql_check = f"SELECT * FROM latlongregion WHERE latitude = {latitude} AND longitude = {longitude}"
        cursor = connection.cursor()
        cursor.execute(sql_check)
        if cursor.fetchone() is None:
            sql_insert = f"""INSERT INTO latlongregion (latitude, longitude, region) VALUES ({latitude}, {longitude}, '{region}')"""
            cursor.execute(sql_insert)
            connection.commit()
            print()
            #print("Address registered successfully")
        else:
            print()
            #print("Address already exists")
    finally:
        cursor.close()
        connection.close()

register_adress(35.0228, -121.36, 'Camaragibe')
