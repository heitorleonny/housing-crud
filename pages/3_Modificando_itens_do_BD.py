import streamlit as st
from bson import ObjectId
## __Todo__!: ajeitar informações
from mongoDB.mongoDB import MongoDBManager


## __Todo__!: remover essas classes e converter em uma só
mongo_database = MongoDBManager()

## __Todo__!: Transformar em listas, assim como na pag 2
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

def create_property_menu(property_id):
    
    # Restante do seu código permanece inalterado
    atributes_apt= [
        'id',  
        'price', 
        'description', 
        'latitude', 
        'longitude', 
        'region_id', 
        'region_name', 
        'state_id', 
        'state_name', 
        'state_abbreviation', 
        'sqfeet', 
        'beds', 
        'baths', 
        'type_id', 
        'type_description', 
        'laundry_option_id', 
        'laundry_option_description', 
        'parking_option_id', 
        'parking_option_description', 
        'combination_id', 
        'cats_allowed', 
        'dogs_allowed', 
        'smoking_allowed', 
        'wheelchair_access', 
        'electric_vehicle_charge', 
        'comes_furnished'
    ]

    apt = MongoDBManager.get_document_by_id(MongoDBManager._get_collection(), property_id)

        # Ajuste para obter o campo 'id' apropriado
    st.write(apt)
    property_id_value = apt.get('_id', None)
    if property_id_value is not None:
        id_show = st.text_input(f"ID", value=str(property_id_value), disabled=True)
    else:
        st.warning("Campo 'id' não encontrado no documento.")
    print(f'\033[41m{apt}\033[0m')
    new_apt = {}
    
    #id_show = st.text_input(f"ID", value=str(apt['_id']), disabled=True)
    #new_apt['desc'] = st.text_area(f"Qual a descrição do imóvel?", value=apt['description'])
    
    col1, col2, col3 = st.columns([1,1,1])
    ## __Todo__!: ajeitar as variáveis padrão e o menu para o formato usado no mongoDB (Como na pag de adição)
    with col1:
        new_apt['type'] =  st.selectbox("Qual o tipo de imóvel?", housing_types, index=(apt['type_id'] - 1) )
        new_apt['region'] = st.text_input(f"Qual a região?")
        new_apt['beds'] = st.number_input(f"Quantos quartos?", value=apt['beds'], step=1, format="%d")
        new_apt['lat'] = st.number_input(f"Qual a latitude do imóvel?", value=float(apt['latitude']) )

    with col2:
        print(apt['laundry_option_id'], laundry_opts)
        new_apt['l_opt'] =  st.selectbox("Qual o tipo de lavanderia?", laundry_opts, index=(apt['laundry_option_id'] - 1) )
        new_apt['state'] =  st.selectbox("Qual o estado?", states, index=(apt['state_id'] - 1) )
        
        new_apt['baths'] = st.number_input(f"Quantos banheiros?", value=apt['baths'], step=1, format="%d")
        new_apt['long'] = st.number_input(f"Qual a longitude do imóvel?", value=float(apt['longitude']))

    with col3:
        new_apt['p_opt'] =  st.selectbox("Qual o tipo de estacionamento?", parking_opts, index=(apt['parking_option_id'] - 1) )
        new_apt['price'] = st.number_input(f"Qual o preço do imóvel?", value=float(apt['price']))
        new_apt['sqfeet'] = st.number_input(f"Qual o tamanho do imóvel? (SqFeet)", value= float(apt['sqfeet']))

    col4, col5, col6 = st.columns([1,1,1])

    with col4:
        new_apt['cats_allowed'] = st.toggle('Permite gatos?', value=apt['cats_allowed'])
        new_apt['wheelchair_access'] = st.toggle('Acessível a cadeira de rodas?', value=apt['wheelchair_access'])

    with col5:
        new_apt['dogs_allowed'] = st.toggle('Permite cachorros?', value=apt['dogs_allowed'])
        new_apt['electric_vehicle_charge'] = st.toggle('Possui carregador para carros elétricos?', value=apt['electric_vehicle_charge'])

    with col6:
        new_apt['smoking_allowed'] = st.toggle('Permite fumar?', value=apt['smoking_allowed'])
        new_apt['comes_furnished'] = st.toggle('Vem mobiliado?', value=apt['comes_furnished']) 

    colum_1, colum_2, colum_3 = st.columns([1,1,7])
    with colum_1:
        if st.button("Editar"):
            print("Saving modifications...")
            
            mongo_database.update_data(
                filter_query={'id': property_id},
                update_query={
                    '$set': {
                        'region_name': new_apt['region'],
                        'state_name': new_apt['state'],
                        'price': new_apt['price'],
                        'description': new_apt['desc'],
                        'latitude': new_apt['lat'],
                        'longitude': new_apt['long'],
                        'property_type': new_apt['type'],
                        'sqfeet': new_apt['sqfeet'],
                        'beds': new_apt['beds'],
                        'baths': new_apt['baths'],
                        'laundry_option': new_apt['l_opt'],
                        'parking_option': new_apt['p_opt'],
                        'cats_allowed': new_apt['cats_allowed'],
                        'dogs_allowed': new_apt['dogs_allowed'],
                        'smoking_allowed': new_apt['smoking_allowed'],
                        'wheelchair_access': new_apt['wheelchair_access'],
                        'electric_vehicle_charge': new_apt['electric_vehicle_charge'],
                        'comes_furnished': new_apt['comes_furnished']
                    }
                }
            )
            with colum_3:
                st.write("Modificações salvas!")

    with colum_2:
        if st.button("Deletar elemento"):
            print("Deletando elemento...")
            # Restante do seu código permanece inalterado
            mongo_database.delete_data({'id': property_id})
            with colum_3:
                st.write("item removido!")

st.write("<h2>Modificando itens do BD<h2>", unsafe_allow_html=True)
st.markdown(f'''Aqui você pode modificar ou deletar itens presentes em seu banco de dados''')

 ## __Todo__!: Fornecer uma lista com todas as propriedades
n_elements = len(list(MongoDBManager.display_documents()))
st.write(n_elements)

if (n_elements > 0):
    cl1, cl2 = st.columns([1,3])
    with cl1:
        id = st.text_input(f"Insira o ID do imóvel")
        if st.button()
        create_property_menu(ObjectId("65d41747e4dde60daf295d50"))

else:
    st.write(f"<h3>Não há nada para editar.<h3>")