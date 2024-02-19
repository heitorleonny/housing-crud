import streamlit as st
import pandas as pd
from database_setup import read_database
import pymysql

atributes_apt= [ "id","region","price","houseType","sqFeet","beds","baths","catsAllowed","dogsAllowed","smokingAllowed","comesFurnished","latitude","longitude" ]
atributes_latlong= [ "Latitude", "Longitude", "Region" ]
atributes_Reg= [ "Region", "State" ]

def join_args(args):
    string = ""

    for i in range(len(args)):
        if i > 0 and args[i] != '':
            string += " and "
        string += args[i]
    return string

def show_results(args , results):
    if len(args) == 0 or len(results) == 0:
        st.table(pd.DataFrame())  # Exibe uma tabela vazia
        print("Nenhum resultado encontrado.")
    else:
        df = pd.DataFrame(results, columns=args)
        st.table(df)


def Create_menu(table):
    if table == "Imóveis":
        table_atributes = atributes_apt
    elif table == "Regiões":
        table_atributes = atributes_Reg
    elif table == "Estados":
        table_atributes = atributes_latlong

    selected_atributes = st.multiselect("Escolha os atributos a serem mostrados", options= table_atributes)

    conditions = []
    lista = st.session_state.get("lista", conditions)
    col1 , col2, col3 = st.columns([1,1,4])

    with col1:
        num_caixas_texto = st.selectbox("Selecione o número de argumentos", options=[1, 2, 3, 4, 5])
        textos = []
        for i in range(num_caixas_texto):
            texto = st.text_input(f"Argumento {i+1}", f"")
            textos.append(texto)
    
    args = textos
    results = []
    with col2:
        if st.button("Gerar pesquisa"):
            print(f"Pesquisando, argumentos: table_atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

            try:
                print(f"Pesquisando, argumentos: table_atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

                if len(selected_atributes) > 0:
                    attributes = read_database.takeAttributes(*selected_atributes)
                    results = (read_database.read_database(selected_atributes, selected_table, join_args(args)))
                else:
                    attributes = read_database.takeAttributes(*table_atributes)
                    results = (read_database.read_database(attributes, selected_table, join_args(args)))
                with col3:
                    show_results(selected_atributes, results)
            except pymysql.err.ProgrammingError:
                st.write("Erro de consulta!")

        if st.button("Mostrar toda a tabela"):
            results = (read_database.read_database("*", selected_table, ''))
            print(f"Pesquisando, argumentos: table_atributes = {table_atributes}\n, argumentos = {''}")
            with col3:
                show_results(table_atributes, results)


#Layout inicial
st.write("<h2>Explorando o database<h2>", unsafe_allow_html=True)
st.markdown(f'''Aqui você pode realizar pesquisas envolvento este banco de dados em uma tabela a sua escolha''')
selected_table = st.selectbox("Qual o tipo de item que você quer pesquisar?", ("Imóveis", "Regiões", "Estados" ))
Create_menu(selected_table)