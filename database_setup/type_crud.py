import mysql.connector
import configparser


class PropertyInfoCRUD:
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

    def create_property_type(self, type_description):
        try:
            query = "INSERT INTO property_type_info (type_description) VALUES (%s)"
            self.cursor.execute(query, (type_description,))
            self.conn.commit()
            print("Tipo de propriedade criado com sucesso.")
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Erro ao criar tipo de propriedade: {err}")

    def read_all_property_types(self):
        try:
            query = "SELECT * FROM property_type_info"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao recuperar tipos de propriedade: {err}")

    def read_property_type_by_id(self, type_id):
        try:
            query = "SELECT * FROM property_type_info WHERE type_id = %s"
            self.cursor.execute(query, (type_id,))
            property_type = self.cursor.fetchone()
            if property_type:
                return property_type
            else:
                print("Tipo de propriedade não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao buscar tipo de propriedade por ID: {err}")

    def update_property_type_description(self, type_id, new_type_description):
        try:
            query = "UPDATE property_type_info SET type_description = %s WHERE type_id = %s"
            self.cursor.execute(query, (new_type_description, type_id))
            self.conn.commit()
            print("Descrição do tipo de propriedade atualizada com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao atualizar descrição do tipo de propriedade: {err}")
            return False

    def delete_property_type(self, type_id):
        try:
            query = "DELETE FROM property_type_info WHERE type_id = %s"
            self.cursor.execute(query, (type_id,))
            self.conn.commit()
            print("Tipo de propriedade excluído com sucesso.")
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao excluir tipo de propriedade: {err}")
            return False
        
    def __end__(self):
        self.cursor.close()
        self.conn.close()
        
if __name__ == '__main__':
    crud = PropertyInfoCRUD()
    print("result:", [item[1] for item in crud.read_all_property_types()])
    