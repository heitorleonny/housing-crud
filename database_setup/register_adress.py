import pymysql

def register_adress(latitude, longitude, region):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="pph1112003",
        database="housing"
    )

    sql = f"""INSERT INTO regionstate (latitude, longitude, region)
             VALUES ({latitude}, {longitude}, '{region}')"""

    cursor = connection.cursor()

register_adress(35.0228, -121.36, 'Camaragibe')
