import streamlit as st
from database_setup.housing_crud import HousingCRUD
from database_setup.region_crud import RegionInfoCRUD
from database_setup.type_crud import PropertyInfoCRUD
from database_setup.laundry_crud import LaundryOptionsInfoCRUD
from database_setup.parking_crud import ParkingOptionsInfoCRUD
from database_setup.state_crud import StateInfoCRUD
import pymysql

#Ainda precisa fazer:
# Permitir atualização da pag de alguma forma (Talvez reescrevendo a pag?)
# Lista de possibilidades deve atalizar após adição de nova região

def create_add_menu():
    region_crud = RegionInfoCRUD()
    state_crud = StateInfoCRUD()
    type_crud = PropertyInfoCRUD()
    laundry_crud = LaundryOptionsInfoCRUD()
    parking_crud = ParkingOptionsInfoCRUD()
    housing_crud = HousingCRUD()
    
    st.write("<h2>Adicionar dados</h2>", unsafe_allow_html=True)
    st.markdown(f'''Aqui você pode adicionar novos imóveis ou regiões no banco de dados, apenas insira os dados e depois aperte no botão para realizar a ação''')

    #Aqui para apartamentos:
    st.write("<h4>Novo imóvel</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

    # Formato das infos: [estado/região, tipo de imóvel, tamanho, quantos quartos, quantos banheiros, Permite gatos, permite cachorros, Permite fumar?, acessível a cadeira de rodas, carregador para carros elétricos, vem mobiliado, latitude, longitude, preço ]
    new_apt = {}

    housing_types = [item[1] for item in type_crud.read_all_property_types()]
    regions = [item[1] for item in region_crud.read_all_regions()]
    states = [item[1] for item in state_crud.read_all_states()]
    laundry_opts = [item[1] for item in laundry_crud.read_all_laundry_options()]
    parking_opts = [item[1] for item in parking_crud.read_all_parking_options()]
    
    new_apt['desc'] = st.text_area(f"Qual a descrição do imóvel?")
    
    col1, col2, col3 = st.columns([1,1,1])
    #Para perguntas de "Sim ou Não" serão usados os valores 0 e 1, referindo-se a não e sim respectivamente
    with col1:
        new_apt['type'] =  st.selectbox("Qual o tipo de imóvel?", housing_types, index=0 )
        new_apt['region'] = st.selectbox(f"Qual a região?", options= regions)
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

    #Ainda precisa ser implementado:
# Formato das infos: [estado/região, tipo de imóvel, tamanho, quantos quartos, quantos banheiros, Permite gatos, permite cachorros, Permite fumar?, acessível a cadeira de rodas, carregador para carros elétricos, vem mobiliado, latitude, longitude, preço ]
    if st.button("Adicionar novo apartamento"):
        print(f" informações : {new_apt}")

        housing_crud.add_property(
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
            laundry_option=new_apt['l_pot'],
            parking_option=new_apt['p_opt'],
            cats_allowed=new_apt['cats_allowed'],
            dogs_allowed=new_apt['dogs_allowed'],
            smoking_allowed=new_apt['smoking_allowed'],
            wheelchair_access=new_apt['wheelchair_access'],
            electric_vehicle_charge=new_apt['electric_vehicle_charge'],
            comes_furnished=new_apt['comes_furnished']
        )


    #Aqui para nova região/Estado:

    st.write("<h4>Nova Região</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

    new_region = ''
    cl1 , cl2, cl3= st.columns([3, 1.5, 3])

    with cl1:
        new_region = st.text_input(f"Qual o nome do novo estado/região?")

    if st.button("Adicionar nova região"):
        regions.append(new_region)
        try:
            region_crud.create_region(new_region)
            print(f" informações : {new_region}")
        except pymysql.err.IntegrityError:
            print("Erro de integridade")


create_add_menu()