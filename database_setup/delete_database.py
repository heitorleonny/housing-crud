def delete_database(command):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "ferraz2013",
        database = "housing"
    )

    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

    cursor.close()
    connection.close()