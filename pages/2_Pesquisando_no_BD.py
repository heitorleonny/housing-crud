import streamlit as st
import pandas as pd
from mongoDB.mongoDB import MongoDBManager


## __Todo__!:Revise se essas características condizem com as características de um item no mongo, pois alguns IDS ou itens podem ser 
## representados de forma diferente no mongoDB, um exemplo é o 'parking_option_id', que não existe mais, 
atributes_apt= [
    "_id",
    "region_name",
    "state_name",
    "price",
    "description",
    "latitude",
    "longitude",
    "property_type",
    "sqfeet",
    "beds",
    "baths",
    "laundry_option",
    "parking_option",
    "cats_allowed",
    "dogs_allowed",
    "smoking_allowed",
    "wheelchair_access",
    "electric_vehicle_charge",
    "comes_furnished"
]


operations= [
    "=", 
    "!=", 
    ">=", 
    "<=", 
    "LIKE", 
]


## __Todo__!: Deixe isso para o final, mas você vai ter que adaptar essa função para receber os resultados de fornecidos na pesquisa e só exibir os atributos selecionados
## se os resultados ou os argumentos forem vazios, exiba uma tabela vazia
def show_results(results, selected_attributes):
    error = False
    if not results:  # Verifica se a lista de resultados está vazia
        st.write("Nenhum resultado encontrado.")
        error = True
    df = pd.DataFrame(results)

    # Selecionar apenas as colunas especificadas
    try:
        df = df[selected_attributes]
    except KeyError:
        error = True

    # Exibir a tabela no Streamlit
    if not error:
        st.table(df)
        



def Create_menu():
    mongo_database = MongoDBManager()

    selected_atributes = st.multiselect("Escolha os atributos a serem mostrados", options=atributes_apt)
    col1 , col2 = st.columns([1,1])

    with col1:
        col11 , col12, col13 = st.columns([1,1,1])
        with col11:
            param = st.selectbox(f"Parâmetro", atributes_apt, index=0)
        with col12:
            op = st.selectbox(f"Operação", operations, index=0)
        with col13:
            value = st.text_input(f"Valor", f"")
    
    results = []
    with col2:
        col21 , col22 = st.columns([1,1])
        with col21:
            if st.button("Gerar pesquisa"):

                ###########################################################################################################################################
                ## __Todo__!: Aqui você precisa modificar se necessário para enviar as condições de busca (Preço > 1000, por exemplo)
                ## em um formato bom parra você

                ###########################################################################################################################################
                try:
                    results = mongo_database.search_documents_with_filter( param , op , value)
                    
                except:
                    st.write("Erro na consulta!")

                with col2:
                     show_results( results, selected_atributes) 

                    ###########################################################################################################################################
        
        ## __Todo__!: Aqui você tem que mostrar todos os imóveis possíveis
        with col22:
            if st.button("Mostrar toda a tabela"):
                results = list(mongo_database.display_documents())           
                print(f"Pesquisando, argumentos: table_atributes = {atributes_apt}\n, argumentos = {''}")
                with col2:
                    show_results(results, atributes_apt)       


#Layout inicial
st.write("<h2>Explorando o database<h2>", unsafe_allow_html=True)
st.markdown(f'''Aqui você pode realizar pesquisas envolvento este banco de dados em uma tabela a sua escolha''')
Create_menu()