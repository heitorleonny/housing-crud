import pymysql

def create_tables():
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "root1234",
        database = "housing"   #precisa criar o shcema no banco  
    )

    cursor = connection.cursor()
    create_query_imovel = """
CREATE TABLE imovel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    endereco VARCHAR(255) NOT NULL,
    numero INT,
    quartos INT,
    banheiros INT,
    area FLOAT,
    preco DECIMAL(10, 2)
);
"""
    cursor.execute(create_query_imovel)
    connection.commit() # sempre usar isso pq ele salva as alterações


    
    
    cursor.close()
    connection.close()