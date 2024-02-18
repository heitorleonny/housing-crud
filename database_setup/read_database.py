import pymysql


def read_database():
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "ferraz2013",
        database = "housing"
    )
    
    attributes = input().split()
    table = input()
    condition = input()

    print(','.join(attributes))

    sql = f""" SELECT {','.join(attributes)}
    FROM {table}
    WHERE {condition};
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    for r in result:
        print(r)

    cursor.close()
    connection.close()

read_database()