import pymysql

def populate_database():
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "root1234",
        database = "housing"
    )

    cursor = connection.cursor()

    #criar comando para popular as tabelas -> cria um intem e pede pro gpt criar cerca de 20 vcs decidem

    cursor.close()
    connection.close()