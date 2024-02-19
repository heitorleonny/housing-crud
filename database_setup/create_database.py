import mysql.connector
from mysql.connector import Error
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read("./database_setup/config.cfg")
    return config["mysql"]

def connect():
    config = read_config()
    try:
        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"]
        )
        if connection.is_connected():
            print("Conexão ao MySQL bem-sucedida.")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def schema_exists(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    for database in databases:
        if 'housing' in database:
            return True
    return False

def create_schema(connection):
    try:
        with open("./database_setup/create_schema.sql", "r") as file:
            sql_script = file.read()
            cursor = connection.cursor()
            for statement in sql_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)
            cursor.execute(
    """
    CREATE TRIGGER insert_listing_info_trigger
    AFTER INSERT ON listing_info
    FOR EACH ROW
    BEGIN
        -- Verificar se o estado da listagem está na tabela state_info
        IF NOT EXISTS (SELECT 1 FROM state_info WHERE state_id = NEW.state_id) THEN
            -- Se não existir, lançar um erro
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'O estado da listagem não está na tabela state_info';
        END IF;

        -- Verificar se a região da listagem está na tabela region_info
        IF NOT EXISTS (SELECT 1 FROM region_info WHERE region_id = NEW.region_id) THEN
            -- Se não existir, lançar um erro
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A região da listagem não está na tabela region_info';
        END IF;

        -- Verificar se o tipo de propriedade da listagem está na tabela property_type_info
        IF NOT EXISTS (SELECT 1 FROM property_type_info WHERE type_id = (SELECT type_id FROM property_info WHERE id = NEW.id)) THEN
            -- Se não existir, lançar um erro
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'O tipo de propriedade da listagem não está na tabela property_type_info';
        END IF;

        -- Verificar se a combinação de amenidades da listagem está na tabela amenity_combinations
        IF NOT EXISTS (SELECT 1 FROM amenity_combinations WHERE combination_id = (SELECT combination_id FROM amenities_info WHERE id = NEW.id)) THEN
            -- Se não existir, lançar um erro
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A combinação de amenidades da listagem não está na tabela amenity_combinations';
        END IF;

        -- Verificar se a opção de lavanderia da listagem está na tabela laundry_options_info
        IF NOT EXISTS (SELECT 1 FROM laundry_options_info WHERE laundry_option_id = (SELECT laundry_option_id FROM amenities_info WHERE id = NEW.id)) THEN
            -- Se não existir, lançar um erro
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A opção de lavanderia da listagem não está na tabela laundry_options_info';
        END IF;

        -- Verificar se a opção de estacionamento da listagem está na tabela parking_options_info
        IF NOT EXISTS (SELECT 1 FROM parking_options_info WHERE parking_option_id = (SELECT parking_option_id FROM amenities_info WHERE id = NEW.id)) THEN
            -- Se não existir, lançar um erro
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A opção de estacionamento da listagem não está na tabela parking_options_info';
        END IF;
    END
    """
            )
            connection.commit()
            cursor.close()
        print("Schema do banco de dados criado com sucesso.")
    except Error as e:
        print(f"Erro ao criar schema do banco de dados: {e}")

def main(force_create=False):
    connection = connect()
    if connection:
        if not schema_exists(connection) or force_create:
            create_schema(connection)
        else:
            print("O esquema 'housing' já existe.")
        connection.close()
        print("Conexão ao MySQL fechada.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--force_create', action='store_true', help='Forçar a criação do esquema')
    args = parser.parse_args()
    main(args.force_create)
