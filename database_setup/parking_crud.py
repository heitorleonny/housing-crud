import mysql.connector
import configparser

class ParkingOptionsInfoCRUD:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("./database_setup/config.cfg")
        params = config["mysql"]
    
        self.conn = mysql.connector.connect(
            host=params["host"],
            user=params["user"],
            password=params["password"],
            database='housing'
        )
        self.cursor = self.conn.cursor()

    def create_parking_option(self, parking_option_description):
        try:
            query = "INSERT INTO parking_options_info (parking_option_description) VALUES (%s)"
            self.cursor.execute(query, (parking_option_description,))
            self.conn.commit()
            print("Opção de estacionamento criada com sucesso.")
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao criar opção de estacionamento: {err}")

    def read_all_parking_options(self):
        try:
            query = "SELECT * FROM parking_options_info"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao recuperar opções de estacionamento: {err}")

    def read_parking_option_by_id(self, parking_option_id):
        try:
            query = "SELECT * FROM parking_options_info WHERE parking_option_id = %s"
            self.cursor.execute(query, (parking_option_id,))
            parking_option = self.cursor.fetchone()
            if parking_option:
                return parking_option
            else:
                print("Opção de estacionamento não encontrada.")
        except mysql.connector.Error as err:
            print(f"Erro ao buscar opção de estacionamento por ID: {err}")

    def update_parking_option_description(self, parking_option_id, new_parking_option_description):
        try:
            query = "UPDATE parking_options_info SET parking_option_description = %s WHERE parking_option_id = %s"
            self.cursor.execute(query, (new_parking_option_description, parking_option_id))
            self.conn.commit()
            print("Descrição da opção de estacionamento atualizada com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar descrição da opção de estacionamento: {err}")
            return False

    def delete_parking_option(self, parking_option_id):
        try:
            query = "DELETE FROM parking_options_info WHERE parking_option_id = %s"
            self.cursor.execute(query, (parking_option_id,))
            self.conn.commit()
            print("Opção de estacionamento excluída com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao excluir opção de estacionamento: {err}")
            return False

    def __del__(self):
        self.cursor.close()
        self.conn.close()
