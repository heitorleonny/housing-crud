import pymysql


def read_database(command):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "ferraz2013",
        database = "housing"
    )

    cursor = connection.cursor()
    cursor.execute(command)
    result = cursor.fetchall()
    
    cursor.close()
    connection.close()

    for r in result:
       print(r)

selectallprincipaltbl = "SELECT * FROM PRINCIPAL;"

read_database(selectallprincipaltbl)