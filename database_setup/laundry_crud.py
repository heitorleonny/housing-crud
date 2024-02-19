import mysql.connector
import configparser

class LaundryOptionsInfoCRUD:
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

    def create_laundry_option(self, laundry_option_description):
        try:
            query = "INSERT INTO laundry_options_info (laundry_option_description) VALUES (%s)"
            self.cursor.execute(query, (laundry_option_description,))
            self.conn.commit()
            print("Opção de lavanderia criada com sucesso.")
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao criar opção de lavanderia: {err}")

    def read_all_laundry_options(self):
        try:
            query = "SELECT * FROM laundry_options_info"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao recuperar opções de lavanderia: {err}")

    def read_laundry_option_by_id(self, laundry_option_id):
        try:
            query = "SELECT * FROM laundry_options_info WHERE laundry_option_id = %s"
            self.cursor.execute(query, (laundry_option_id,))
            laundry_option = self.cursor.fetchone()
            if laundry_option:
                return laundry_option
            else:
                print("Opção de lavanderia não encontrada.")
        except mysql.connector.Error as err:
            print(f"Erro ao buscar opção de lavanderia por ID: {err}")

    def update_laundry_option_description(self, laundry_option_id, new_laundry_option_description):
        try:
            query = "UPDATE laundry_options_info SET laundry_option_description = %s WHERE laundry_option_id = %s"
            self.cursor.execute(query, (new_laundry_option_description, laundry_option_id))
            self.conn.commit()
            print("Descrição da opção de lavanderia atualizada com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar descrição da opção de lavanderia: {err}")
            return False

    def delete_laundry_option(self, laundry_option_id):
        try:
            query = "DELETE FROM laundry_options_info WHERE laundry_option_id = %s"
            self.cursor.execute(query, (laundry_option_id,))
            self.conn.commit()
            print("Opção de lavanderia excluída com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao excluir opção de lavanderia: {err}")
            return False

