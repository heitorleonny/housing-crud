import pymysql
from random import randint

def generate_id():
    return randint(1, 4294967295)

def create_property(region, price, houseType, sqfeet, beds, baths, catsAllowed, dogsAllowed, smokingAllowed, comesFurnished, latitude, longitude):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="ferraz2013",
        database="housing"
    )

    sql = f"""INSERT INTO PRINCIPAL (id, region, price, houseType, sqfeet, beds, baths, catsAllowed, dogsAllowed, smokingAllowed, comesFurnished, latitude, longitude)
             VALUES ({generate_id()}, '{region}', {price}, '{houseType}', {sqfeet}, {beds}, {baths}, {catsAllowed}, {dogsAllowed}, {smokingAllowed}, {comesFurnished}, {latitude}, {longitude})"""

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()  # Commita as alterações

    cursor.close()
    connection.close()

create_property("stockton", 1264, "apartment", 830, 2, 1, 1, 1, 1, 0, 38.0228, -121.361)
