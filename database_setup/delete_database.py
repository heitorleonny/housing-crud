def delete_database(command):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "popopipiska",
        database = "housing"
    )

    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

    cursor.close()
    connection.close()