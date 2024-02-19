import streamlit as st
from database_setup.housing_crud import HousingCRUD
from database_setup.region_crud import RegionInfoCRUD
from database_setup.type_crud import PropertyInfoCRUD
from database_setup.laundry_crud import LaundryOptionsInfoCRUD
from database_setup.parking_crud import ParkingOptionsInfoCRUD
from database_setup.state_crud import StateInfoCRUD

region_crud = RegionInfoCRUD()
state_crud = StateInfoCRUD()
type_crud = PropertyInfoCRUD()
laundry_crud = LaundryOptionsInfoCRUD()
parking_crud = ParkingOptionsInfoCRUD()
housing_crud = HousingCRUD()

housing_types = [item[1] for item in type_crud.read_all_property_types()]
regions = [item[1] for item in region_crud.read_all_regions()]
states = [item[1] for item in state_crud.read_all_states()]
laundry_opts = [item[1] for item in laundry_crud.read_all_laundry_options()]
parking_opts = [item[1] for item in parking_crud.read_all_parking_options()]

def create_property_menu(id):    
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


    apt = dict(zip(atributes_apt, housing_crud.search_property(id={'op': '=', 'value': id})[0]))
    print(f'\033[41m{apt}\033[0m')
    new_apt = {}
    
    id_show = st.text_input(f"ID", value=apt['id'], disabled=True)
    
    new_apt['desc'] = st.text_area(f"Qual a descrição do imóvel?",value=apt['description'])
    
    col1, col2, col3 = st.columns([1,1,1])
    #Para perguntas de "Sim ou Não" serão usados os valores 0 e 1, referindo-se a não e sim respectivamente
    with col1:
        new_apt['type'] =  st.selectbox("Qual o tipo de imóvel?", housing_types, index=(apt['type_id'] - 1) )
        new_apt['region'] = st.selectbox(f"Qual a região?", options= regions, index=(apt['region_id'] - 1))
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
            housing_crud.update_property(
                property_id=id,
                region_name=new_apt['region'],
                state_name=new_apt['state'],
                price=new_apt['price'],
                description=new_apt['desc'],
                latitude=new_apt['lat'],
                longitude=new_apt['long'],
                property_type=new_apt['type'],
                sqfeet=new_apt['sqfeet'],
                beds=new_apt['beds'],
                baths=new_apt['baths'],
                laundry_option=new_apt['l_opt'],
                parking_option=new_apt['p_opt'],
                cats_allowed=new_apt['cats_allowed'],
                dogs_allowed=new_apt['dogs_allowed'],
                smoking_allowed=new_apt['smoking_allowed'],
                wheelchair_access=new_apt['wheelchair_access'],
                electric_vehicle_charge=new_apt['electric_vehicle_charge'],
                comes_furnished=new_apt['comes_furnished']
            )
            with colum_3:
                st.write("Modificações salvas!")
    with colum_2:
        if st.button("Deletar elemento"):
            print("Deletando elemento...")
            housing_crud.remove_property(id)
            with colum_3:
                st.write("item removido!")

st.write("<h2>Modificando itens do BD<h2>", unsafe_allow_html=True)
st.markdown(f'''Aqui você pode modificar ou deletar itens presentes em seu banco de dados''')
n_elements = len(housing_crud.search_all_properties())
if (n_elements > 0):
    cl1, cl2 = st.columns([1,3])
    with cl1:
        id = st.number_input(f"Insira o ID do imóvel", value=1, min_value = 1, max_value=n_elements)
    create_property_menu(id)
else:
    st.write(f"<h3>Não há nada para editar.<h3>")