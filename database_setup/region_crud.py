import mysql.connector
import configparser


class RegionInfoCRUD:
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

    def create_region(self, region_name):
        try:
            query = "INSERT INTO region_info (region_name) VALUES (%s)"
            self.cursor.execute(query, (region_name,))
            self.conn.commit()
            print("Região criada com sucesso.")
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao criar região: {err}")

    def read_all_regions(self):
        try:
            query = "SELECT * FROM region_info"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao recuperar regiões: {err}")
    
    def read_region_by_id(self, region_id):
        try:
            query = "SELECT * FROM region_info WHERE region_id = %s"
            self.cursor.execute(query, (region_id,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Erro ao buscar região por ID: {err}")

    def update_region_name(self, region_id, new_region_name):
        try:
            query = "UPDATE region_info SET region_name = %s WHERE region_id = %s"
            self.cursor.execute(query, (new_region_name, region_id))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar nome da região: {err}")
            return False

    def delete_region(self, region_id):
        try:
            query = "DELETE FROM region_info WHERE region_id = %s"
            self.cursor.execute(query, (region_id,))
            self.conn.commit()
            print("Região excluída com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao excluir região: {err}")
            return False

    def __end__(self):
        self.cursor.close()
        self.conn.close()
        
if __name__ == '__main__':
    crud = RegionInfoCRUD()
    print("result:", [item[1] for item in crud.read_all_regions()])
    