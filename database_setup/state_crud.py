import mysql.connector
import configparser

class StateInfoCRUD:
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

    def create_state(self, state_name, state_abbreviation):
        try:
            query = "INSERT INTO state_info (state_name, state_abbreviation) VALUES (%s, %s)"
            self.cursor.execute(query, (state_name, state_abbreviation))
            self.conn.commit()
            print("Estado criado com sucesso.")
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao criar estado: {err}")

    def read_all_states(self):
        try:
            query = "SELECT * FROM state_info"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao recuperar estados: {err}")

    def read_state_by_id(self, state_id):
        try:
            query = "SELECT * FROM state_info WHERE id = %s"
            self.cursor.execute(query, (state_id,))
            state = self.cursor.fetchone()
            if state:
                return state
            else:
                print("Estado não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao buscar estado por ID: {err}")

    def update_state(self, state_id, state_name, state_abbreviation):
        try:
            query = "UPDATE state_info SET state_name = %s, state_abbreviation = %s WHERE id = %s"
            self.cursor.execute(query, (state_name, state_abbreviation, state_id))
            self.conn.commit()
            print("Estado atualizado com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar estado: {err}")
            return False

    def delete_state(self, state_id):
        try:
            query = "DELETE FROM state_info WHERE id = %s"
            self.cursor.execute(query, (state_id,))
            self.conn.commit()
            print("Estado excluído com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao excluir estado: {err}")
            return False

