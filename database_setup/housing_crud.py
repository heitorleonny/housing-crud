import mysql.connector
import configparser

class HousingCRUD:
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

    def add_property(self, region_name, state_name, price, description, latitude, longitude, property_type, sqfeet, beds, baths, laundry_option, parking_option, cats_allowed, dogs_allowed, smoking_allowed, wheelchair_access, electric_vehicle_charge, comes_furnished):
        try:
            # Verificar se a região existe, se não, adicionar
            self.cursor.execute("SELECT region_id FROM region_info WHERE region_name = %s", (region_name,))
            region = self.cursor.fetchone()
            if not region:
                raise ValueError("Região não encontrada na base de dados.")
            else:
                region_id = region[0]

            # Verificar se o estado existe, se não, lançar um erro
            self.cursor.execute("SELECT state_id FROM state_info WHERE state_name = %s", (state_name,))
            state = self.cursor.fetchone()
            if not state:
                raise ValueError("Estado não encontrado na base de dados.")

            # Inserir dados da propriedade
            self.cursor.execute("""
                INSERT INTO listing_info (region_id, state_id, price, description, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (region_id, state[0], price, description, latitude, longitude))
            self.conn.commit()
            listing_id = self.cursor.lastrowid

            # Obter o id do tipo de propriedade
            self.cursor.execute("SELECT type_id FROM property_type_info WHERE type_description = %s", (property_type,))
            property_type_id = self.cursor.fetchone()
            
            if not property_type_id:
                raise ValueError("Tipo não encontrado na base de dados.")

            # Inserir dados específicos da propriedade
            self.cursor.execute("""
                INSERT INTO property_info (id, type_id, sqfeet, beds, baths)
                VALUES (%s, %s, %s, %s, %s)
            """, (listing_id, property_type_id[0], sqfeet, beds, baths))
            self.conn.commit()

            # Obter o id da opção de lavanderia
            self.cursor.execute("SELECT laundry_option_id FROM laundry_options_info WHERE laundry_option_description = %s", (laundry_option,))
            laundry_option_id = self.cursor.fetchone()
            if not laundry_option_id:
                raise ValueError("laundry option não encontrado na base de dados.")

            # Obter o id da opção de estacionamento
            self.cursor.execute("SELECT parking_option_id FROM parking_options_info WHERE parking_option_description = %s", (parking_option,))
            parking_option_id = self.cursor.fetchone()
            if not parking_option_id:
                raise ValueError("parking option não encontrado na base de dados.")

            # Obter o id da combinação de amenidades
            self.cursor.execute("""
                SELECT combination_id
                FROM amenity_combinations
                WHERE cats_allowed = %s AND dogs_allowed = %s AND smoking_allowed = %s
                AND wheelchair_access = %s AND electric_vehicle_charge = %s AND comes_furnished = %s
            """, (cats_allowed, dogs_allowed, smoking_allowed, wheelchair_access, electric_vehicle_charge, comes_furnished))
            combination_id = self.cursor.fetchone()[0]

            # Inserir dados de amenidades
            self.cursor.execute("""
                INSERT INTO amenities_info (id, combination_id, laundry_option_id, parking_option_id)
                VALUES (%s, %s, %s, %s)
            """, (listing_id, combination_id, laundry_option_id[0], parking_option_id[0]))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Erro ao adicionar propriedade: {str(e)}")
    
    def remove_property(self, property_id):
        try:
            with self.conn.cursor() as cursor:
                # Delete the property
                cursor.execute("DELETE FROM listing_info WHERE id = %s", (property_id,))
                cursor.execute("UPDATE listing_info SET id = id - 1 WHERE id > %s;", (property_id,))
            self.conn.commit()
        except mysql.connector.Error as e:
            self.conn.rollback()
            raise Exception(f"Error removing property: {str(e)}")   
            
        print("Propriedade removida com sucesso.")
        

    def update_property(self, property_id, region_name=None, state_name=None, price=None, description=None, latitude=None, longitude=None, property_type=None, sqfeet=None, beds=None, baths=None, laundry_option=None, parking_option=None, cats_allowed=None, dogs_allowed=None, smoking_allowed=None, wheelchair_access=None, electric_vehicle_charge=None, comes_furnished=None):
        try:
            # Verificar se já existe uma transação em andamento
            if not self.conn.in_transaction:
                # Se não houver, iniciar uma nova transação
                self.conn.start_transaction()

            # Atualizar dados da listagem
            if region_name or state_name or price is not None or description or latitude is not None or longitude is not None:
                update_query = "UPDATE listing_info SET "
                values = []

                if region_name:
                    self.cursor.execute("SELECT region_id FROM region_info WHERE region_name = %s", (region_name,))
                    region = self.cursor.fetchone()
                    if not region:
                        raise ValueError("Região não encontrada na base de dados.")
                    else:
                        region_id = region[0]
                    update_query += "region_id = %s, "
                    values.append(region_id)

                if state_name:
                    self.cursor.execute("SELECT state_id FROM state_info WHERE state_name = %s", (state_name,))
                    state = self.cursor.fetchone()
                    if not state:
                        raise ValueError("Estado não encontrado na base de dados.")
                    update_query += "state_id = %s, "
                    values.append(state[0])

                if price is not None:
                    update_query += "price = %s, "
                    values.append(price)

                if description:
                    update_query += "description = %s, "
                    values.append(description)

                if latitude is not None:
                    update_query += "latitude = %s, "
                    values.append(latitude)

                if longitude is not None:
                    update_query += "longitude = %s, "
                    values.append(longitude)

                # Remover a última vírgula e espaço
                update_query = update_query[:-2]

                update_query += " WHERE id = %s"
                values.append(property_id)

                self.cursor.execute(update_query, tuple(values))

            # Atualizar dados específicos da propriedade
            if property_type or sqfeet is not None or beds is not None or baths is not None:
                if property_type:
                    self.cursor.execute("SELECT type_id FROM property_type_info WHERE type_description = %s", (property_type,))
                    property_type_id = self.cursor.fetchone()[0]
                    self.cursor.execute("UPDATE property_info SET type_id = %s WHERE id = %s", (property_type_id, property_id))

                if sqfeet is not None:
                    self.cursor.execute("UPDATE property_info SET sqfeet = %s WHERE id = %s", (sqfeet, property_id))

                if beds is not None:
                    self.cursor.execute("UPDATE property_info SET beds = %s WHERE id = %s", (beds, property_id))

                if baths is not None:
                    self.cursor.execute("UPDATE property_info SET baths = %s WHERE id = %s", (baths, property_id))

            # Atualizar dados de amenidades
            if laundry_option or parking_option or cats_allowed is not None or dogs_allowed is not None or smoking_allowed is not None or wheelchair_access is not None or electric_vehicle_charge is not None or comes_furnished is not None:
                self.cursor.execute("""
                    SELECT combination_id
                    FROM amenity_combinations
                    WHERE cats_allowed = %s AND dogs_allowed = %s AND smoking_allowed = %s
                    AND wheelchair_access = %s AND electric_vehicle_charge = %s AND comes_furnished = %s
                """, (cats_allowed, dogs_allowed, smoking_allowed, wheelchair_access, electric_vehicle_charge, comes_furnished))
                combination_id = self.cursor.fetchone()[0]

                if laundry_option:
                    self.cursor.execute("SELECT laundry_option_id FROM laundry_options_info WHERE laundry_option_description = %s", (laundry_option,))
                    laundry_option_id = self.cursor.fetchone()[0]
                    self.cursor.execute("UPDATE amenities_info SET laundry_option_id = %s WHERE id = %s", (laundry_option_id, property_id))

                if parking_option:
                    self.cursor.execute("SELECT parking_option_id FROM parking_options_info WHERE parking_option_description = %s", (parking_option,))
                    parking_option_id = self.cursor.fetchone()[0]
                    self.cursor.execute("UPDATE amenities_info SET parking_option_id = %s WHERE id = %s", (parking_option_id, property_id))

                self.cursor.execute("UPDATE amenities_info SET combination_id = %s WHERE id = %s", (combination_id, property_id))

            # Confirmar transação
            self.conn.commit()
            print("Propriedade atualizada com sucesso.")

        except Exception as e:
            # Reverter alterações em caso de erro
            self.conn.rollback()
            print("Erro ao atualizar propriedade:", str(e))


    def search_property(self, **kwargs):
        conditions = []
        values = []

        for key, value in kwargs.items():
            if key == 'id':
                conditions.append(f"property_info.id {value['op']} %s")  
            elif key == 'region_id':
                conditions.append(f"region_info.region_id {value['op']} %s")
            elif key == 'state_id':
                conditions.append(f"state_info.state_id {value['op']} %s")
            elif key == 'type_id':
                conditions.append(f"property_type_info.type_id {value['op']} %s")
            elif key == 'laundry_option_id':
                conditions.append(f"laundry_options_info.laundry_option_id {value['op']} %s")
            elif key == 'parking_option_id':
                conditions.append(f"parking_options_info.parking_option_id {value['op']} %s")
            elif key == 'combination_id':
                conditions.append(f"amenity_combinations.combination_id {value['op']} %s")
            else:
                conditions.append(f"{key} {value['op']} %s")
            values.append(value['value'])

        query = f"""
            SELECT *
            FROM listing_info INNER JOIN region_info ON listing_info.region_id = region_info.region_id INNER JOIN state_info ON listing_info.state_id = state_info.state_id
            INNER JOIN property_info ON listing_info.id = property_info.id INNER JOIN property_type_info ON property_info.type_id = property_type_info.type_id
            INNER JOIN amenities_info ON listing_info.id = amenities_info.id INNER JOIN laundry_options_info ON amenities_info.laundry_option_id = laundry_options_info.laundry_option_id  INNER JOIN parking_options_info ON amenities_info.parking_option_id = parking_options_info.parking_option_id INNER JOIN amenity_combinations ON amenities_info.combination_id = amenity_combinations.combination_id
            WHERE {' AND '.join(conditions)}
        """
        self.cursor.execute(query, values)
        results = self.cursor.fetchall()
        ret = [[j for j in i] for i in results]

        for i in range(len(ret)):
            ret[i].pop(22)
            ret[i].pop(21)
            ret[i].pop(20)
            ret[i].pop(19)
            ret[i].pop(13)
            ret[i].pop(12)
            ret[i].pop(2)
            ret[i].pop(1) 
        return ret

    def search_all_properties(self):
        query = """
            SELECT *
            FROM listing_info INNER JOIN region_info ON listing_info.region_id = region_info.region_id INNER JOIN state_info ON listing_info.state_id = state_info.state_id
            INNER JOIN property_info ON listing_info.id = property_info.id INNER JOIN property_type_info ON property_info.type_id = property_type_info.type_id
            INNER JOIN amenities_info ON listing_info.id = amenities_info.id INNER JOIN laundry_options_info ON amenities_info.laundry_option_id = laundry_options_info.laundry_option_id  INNER JOIN parking_options_info ON amenities_info.parking_option_id = parking_options_info.parking_option_id INNER JOIN amenity_combinations ON amenities_info.combination_id = amenity_combinations.combination_id
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        ret = [[j for j in i] for i in results]

        for i in range(len(ret)):
            ret[i].pop(22)
            ret[i].pop(21)
            ret[i].pop(20)
            ret[i].pop(19)
            ret[i].pop(13)
            ret[i].pop(12)
            ret[i].pop(2)
            ret[i].pop(1) 
        return ret

    def __end__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    crud = HousingCRUD()
    print(crud.search_property(combination_id={'op': '=', 'value': 1}))