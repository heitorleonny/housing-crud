import streamlit as st

# __Todo__!: Ajeitar importações
from mongoDB.mongoDB import MongoDBManager



def create_add_menu():
    
    mongo_database = MongoDBManager()
    
    st.write("<h2>Adicionar dados</h2>", unsafe_allow_html=True)
    st.markdown(f'''Aqui você pode adicionar novos imóveis ou regiões no banco de dados, apenas insira os dados e depois aperte no botão para realizar a ação''')

    #Aqui para apartamentos:
    st.write("<h4>Novo imóvel</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

    new_apt = {}


    ##__Todo__!: Aqui são listados os tipos de casas, regiões e fins ou você, uma sujestão seria converter essas listas para listas com as opções disponíveis e listadas
    ## no workbench, como a lista housing_types, que pode virar algo como
    
    housing_types = [ 'apartment', 'condo', 'house', 'duplex', 'townhouse', 'loft', 'manufacturated', 'cottage/cabin', 'flat', 'in-law', 'land', 'assisted living' ]
    laundry_opts = ['w/d in unit', 'w/d hookups', 'laundry on site','laundry in bldg', 'no laundry on site']
    parking_opts = ['carport','attached garage','off-street parking','detached garage','street parking', 'no parking', 'valet parking']
    states = [
'alaska', 
'arizona', 
'arkansas', 
'california',
'colorado',
'connecticut', 
'district of columbia',
'delaware', 
 'florida', 
 'georgia', 
 'hawaii', 
 'idaho', 
 'illinois', 
 'indiana', 
 'iowa', 
 'kansas', 
 'kentucky', 
 'louisiana', 
 'maine', 
 'maryland',
 'massachusetts', 
 'michigan', 
 'minnesota', 
 'mississippi', 
 'missouri', 
 'montana', 
 'nebraska', 
 'nevada', 
 'new hampshire', 
 'new jersey', 
 'new mexico', 
 'new york', 
 'north carolina', 
 'north dakota', 
 'ohio', 
 'oklahoma', 
 'oregon', 
 'pennsylvania', 
 'rhode island', 
 'south carolina', 
 'south dakota', 
 'tennessee', 
 'texas', 
 'utah', 
 'vermont', 
 'virginia', 
 'washington', 
 'west virginia', 
 'wisconsin', 
 'wyoming', 
]
    
    new_apt['desc'] = st.text_area(f"Qual a descrição do imóvel?")
    
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        new_apt['type'] =  st.selectbox("Qual o tipo de imóvel?", housing_types, index=0 )
        new_apt['region'] = st.text_input(f"Qual a região?")
        new_apt['beds'] = st.number_input(f"Quantos quartos?", value=2, step=1, format="%d")
        new_apt['lat'] = st.number_input(f"Qual a latitude do imóvel?", value=39.5483)

    with col2:
        new_apt['l_pot'] =  st.selectbox("Qual o tipo de lavanderia?", laundry_opts, index=0 )
        new_apt['state'] =  st.selectbox("Qual o estado?", states, index=0 )
        
        new_apt['baths'] = st.number_input(f"Quantos banheiros?", value=3, step=1, format="%d")
        new_apt['long'] = st.number_input(f"Qual a longitude do imóvel?", value=-119.746)

    with col3:
        new_apt['p_opt'] =  st.selectbox("Qual o tipo de estacionamento?", parking_opts, index=0 )
        new_apt['price'] = st.number_input(f"Qual o preço do imóvel?", value= 1256.74)
        new_apt['sqfeet'] = st.number_input(f"Qual o tamanho do imóvel? (SqFeet)", value= 750)

    col4, col5, col6 = st.columns([1,1,1])

    with col4:
        new_apt['cats_allowed'] = st.toggle('Permite gatos?')
        new_apt['wheelchair_access'] = st.toggle('Acessível a cadeira de rodas?')

    with col5:
        new_apt['dogs_allowed'] = st.toggle('Permite cachorros?')
        new_apt['electric_vehicle_charge'] = st.toggle('Possui carregador para carros elétricos?')

    with col6:
        new_apt['smoking_allowed'] = st.toggle('Permite fumar?')
        new_apt['comes_furnished'] = st.toggle('Vem mobiliado?') 

    if st.button("Adicionar novo apartamento"):
        print(f" informações : {new_apt}")

    ##__Todo__!: Aqui você vai adicionar a função de inserir algo no DB, você deve usar as características como argumentos para a adição de um novo imóvel
    ## todas as caracteristicas do novo imóvel são armazenadas no dicionário new_apt, então você apenas precisa chamar elas como mostrado abaixo
        try:
            mongo_database.insert_data({
            "region_name": new_apt['region'],
            "state_name": new_apt['state'],
            "price": new_apt['price'],
            "description": new_apt['desc'],
            "latitude": new_apt['lat'],
            "longitude": new_apt['long'],
            "property_type": new_apt['type'],
            "sqfeet": new_apt['sqfeet'],
            "beds": new_apt['beds'],
            "baths": new_apt['baths'],
            "laundry_option": new_apt['l_pot'],
            "parking_option": new_apt['p_opt'],
            "cats_allowed": new_apt['cats_allowed'],
            "dogs_allowed": new_apt['dogs_allowed'],
            "smoking_allowed": new_apt['smoking_allowed'],
            "wheelchair_access": new_apt['wheelchair_access'],
            "electric_vehicle_charge": new_apt['electric_vehicle_charge'],
            "comes_furnished": new_apt['comes_furnished']
        }
        
        )
            st.write("Success on registration")

        except:
            
            st.write("Error on registration")



create_add_menu()