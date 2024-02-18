import pymysql


def takeAttributes(*attributes):
    return attributes

def read_database(attributes,table,condition):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pph1112003",
        database = "housing"
    )
    
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
    return result

attributes = takeAttributes('region', 'price' ,'houseType')
read_database(attributes,'principal', 'price > 1000')