import streamlit as st
import pandas as pd
from database_setup.housing_crud import HousingCRUD
from database_setup.region_crud import RegionInfoCRUD
from database_setup.type_crud import PropertyInfoCRUD
from database_setup.laundry_crud import LaundryOptionsInfoCRUD
from database_setup.parking_crud import ParkingOptionsInfoCRUD
from database_setup.state_crud import StateInfoCRUD
import pymysql

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

operations= [
    "=", 
    "!=", 
    ">=", 
    "<=", 
    "LIKE", 
]

def show_results(args , results, selected = atributes_apt):
    if len(args) == 0 or len(results) == 0:
        st.table(pd.DataFrame())  # Exibe uma tabela vazia
        print("Nenhum resultado encontrado.")
    else:
        df = pd.DataFrame(results, columns=args)
        st.table(df[selected])


def Create_menu():
    housing_crud = HousingCRUD()

    selected_atributes = st.multiselect("Escolha os atributos a serem mostrados", options=atributes_apt)

    conditions = []
    lista = st.session_state.get("lista", conditions)
    col1 , col2 = st.columns([1,2])

    with col1:
        num_caixas_texto = st.selectbox("Selecione o número de argumentos", options=range(1, len(atributes_apt) + 1))
        args = {}
        for i in range(num_caixas_texto):
            col11 , col12, col13 = st.columns([1,1,1])
            with col11:
                param = st.selectbox("Parâmetro", atributes_apt, index=0)
            with col12:
                op = st.selectbox("Operação", operations, index=0)
            with col13:
                value = st.text_input(f"Valor", f"")
            args[param] = {'op': op, 'value': value}
    
    results = []
    with col2:
        col21 , col22 = st.columns([1,1])
        with col21:
            if st.button("Gerar pesquisa"):
                conditions = []
                
                for key, value in args.items():
                    conditions.append(f"{key} {value['op']} {value['value']}")
                
                print(f"Pesquisando, argumentos: table_atributes = {selected_atributes}\n, argumentos = {' AND '.join(conditions)}")

                try:
                    results = housing_crud.search_property(**args)
                    with col2:
                        show_results(atributes_apt, results, selected_atributes)  
                except pymysql.err.ProgrammingError:
                    st.write("Erro de consulta!")
        with col22:
            if st.button("Mostrar toda a tabela"):
                results = housing_crud.search_all_properties()
                    
                print(f"Pesquisando, argumentos: table_atributes = {atributes_apt}\n, argumentos = {''}")
                with col2:
                    show_results(atributes_apt, results)       


#Layout inicial
st.write("<h2>Explorando o database<h2>", unsafe_allow_html=True)
st.markdown(f'''Aqui você pode realizar pesquisas envolvento este banco de dados em uma tabela a sua escolha''')
Create_menu()