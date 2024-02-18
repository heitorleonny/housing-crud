import pymysql

def create_region(region, state):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="ferraz2013",
        database="housing",
    )

    # Verifica se a região já existe
    sql_check = f"""SELECT COUNT(*) FROM regionstate WHERE region = '{region}'"""
    cursor = connection.cursor()
    cursor.execute(sql_check)
    count = cursor.fetchone()[0]

    if count == 0:
        # Insere o registro se não existir
        sql = f"""INSERT INTO regionstate (region, state)
                   VALUES ('{region}', '{state}')"""
        cursor.execute(sql)
        connection.commit()
        #print(f"Região '{region}' inserida com sucesso")

    else:
        print()
        #print(f"Região '{region}' já existe!")

    cursor.close()
    connection.close()


# Exemplo de uso
create_region("Camaragibe", "PE")
create_region("Santos", "São Paulo")
create_region("Igarassu", "PE")

