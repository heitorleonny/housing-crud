import pymysql

def delete_database(command):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pph1112003",
        database = "housing"
    )

    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()

    cursor.close()
    connection.close()

delete_database(input(':'))
