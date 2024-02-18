import streamlit as st
import pandas as pd
from database_setup import read_database
import pymysql


def join_args(args):
    string = ""

    for i in range(len(args)):
        if i > 0:
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


def Create_principal_menu():
    atributes= [ "id","region","price","houseType","sqFeet","beds","baths","catsAllowed","dogsAllowed","smokingAllowed","comesFurnished","latitude","longitude" ]
    selected_atributes = st.multiselect("Escolha os atributos a serem mostrados", options= atributes)

    conditions = []
    lista = st.session_state.get("lista", conditions)
    col1 , col2 = st.columns([1,2])

    with col1:
        num_caixas_texto = st.selectbox("Selecione o número de argumentos", options=[1, 2, 3, 4, 5])
        textos = []
        for i in range(num_caixas_texto):
            texto = st.text_input(f"Argumento {i+1}", f"Insira o argumento {i+1}")
            textos.append(texto)
    
    args = textos
    results = []
    with col2:
        if st.button("Gerar pesquisa"):
            print(f"Pesquisando, argumentos: atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

            try:
                print(f"Pesquisando, argumentos: atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

                attributes = read_database.takeAttributes(*selected_atributes)
                results = (read_database.read_database(attributes, selected_table, join_args(args)))
                show_results(selected_atributes, results)
            except pymysql.err.ProgrammingError:
                st.write("Erro de consulta!")

def Create_regionstate_menu():
    atributes= [ "Region", "State" ]
    selected_atributes = st.multiselect("Escolha os atributos a serem mostrados", options= atributes)

    conditions = []
    lista = st.session_state.get("lista", conditions)
    col1 , col2 = st.columns([1,2])

    with col1:
        num_caixas_texto = st.selectbox("Selecione o número de argumentos", options=[1, 2, 3, 4, 5])
        textos = []
        for i in range(num_caixas_texto):
            texto = st.text_input(f"Argumento {i+1}", f"Insira o argumento {i+1}")
            textos.append(texto)
    
    args = textos
    results = []
    with col2:
        if st.button("Gerar pesquisa"):
            print(f"Pesquisando, argumentos: atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

            try:
                print(f"Pesquisando, argumentos: atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

                attributes = read_database.takeAttributes(*selected_atributes)
                results = (read_database.read_database(attributes, selected_table, join_args(args)))
                show_results(selected_atributes, results)
            except pymysql.err.ProgrammingError:
                st.write("Erro de consulta!")

def Create_latreg_menu():
    atributes= [ "Latitude", "Longitude", "Region" ]
    selected_atributes = st.multiselect("Escolha os atributos a serem mostrados", options= atributes)

    conditions = []
    lista = st.session_state.get("lista", conditions)
    col1 , col2 = st.columns([1,2])

    with col1:
        num_caixas_texto = st.selectbox("Selecione o número de argumentos", options=[1, 2, 3, 4, 5])
        textos = []
        for i in range(num_caixas_texto):
            texto = st.text_input(f"Argumento {i+1}", f"Insira o argumento {i+1}")
            textos.append(texto)
    
    args = textos
    results = []
    with col2:
        if st.button("Gerar pesquisa"):
            print(f"Pesquisando, argumentos: atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

            try:
                print(f"Pesquisando, argumentos: atributes = {selected_atributes}\n, argumentos = {join_args(args)}")

                attributes = read_database.takeAttributes(*selected_atributes)
                results = (read_database.read_database(attributes, selected_table, join_args(args)))
                show_results(selected_atributes, results)
            except pymysql.err.ProgrammingError:
                st.write("Erro de consulta!")


#Layout inicial
st.write("<h2>Explorando o database<h2>", unsafe_allow_html=True)
st.markdown(f'''Aqui você pode realizar pesquisas envolvento este banco de dados em uma tabela a sua escolha''')

selected_table = st.selectbox("Qual tabela você quer pesquisar?", ("PRINCIPAL", "REGIONSTATE", "LATLONGREGION" ))

if selected_table == "PRINCIPAL":
    Create_principal_menu()
elif selected_table == "REGIONSTATE":
    Create_regionstate_menu()
elif selected_table == "LATLONGREGION":
    Create_latreg_menu()