import streamlit as st
import pandas as pd

## __Todo__!: Ajeitar importações

from mongoDB.mongoDB import MongoDBManager


## __Todo__!:Revise se essas características condizem com as características de um item no mongo, pois alguns IDS ou itens podem ser 
## representados de forma diferente no mongoDB, um exemplo é o 'parking_option_id', que não existe mais, 
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


## __Todo__!: Deixe isso para o final, mas você vai ter que adaptar essa função para receber os resultados de fornecidos na pesquisa e só exibir os atributos selecionados
## se os resultados ou os argumentos forem vazios, exiba uma tabela vazia
def show_results(args , results, selected = atributes_apt):
    if len(args) == 0 or len(results) == 0:
        st.table(pd.DataFrame())  # Exibe uma tabela vazia
        print("Nenhum resultado encontrado.")
        st.write("Nenhum resultado encontrado.")
    else:
        df = pd.DataFrame(results, columns=args)
        st.table(df[selected])


def Create_menu():
    mongo_database = MongoDBManager()

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
                param = st.selectbox(f"Parâmetro {i + 1}", atributes_apt, index=0)
            with col12:
                op = st.selectbox(f"Operação {i + 1}", operations, index=0)
            with col13:
                value = st.text_input(f"Valor {i + 1}", f"")
            args[param] = {'op': op, 'value': value}
    
    results = []
    with col2:
        col21 , col22 = st.columns([1,1])
        with col21:
            if st.button("Gerar pesquisa"):

                ###########################################################################################################################################
                ## __Todo__!: Aqui você precisa modificar se necessário para enviar as condições de busca (Preço > 1000, por exemplo)
                ## em um formato bom parra você
                conditions = []
                for key, value in args.items():
                    conditions.append(f"{key} {value['op']} {value['value']}")
                
                print(f"Pesquisando, argumentos: table_atributes = {selected_atributes}\n, argumentos = {' AND '.join(conditions)}")
                ###########################################################################################################################################
                try:
                    
                    ###########################################################################################################################################
                    ## __Todo__!: Aqui você precisa substituir seu código para a função do mongodb de busca, aceitando as condições 'arga' como argumentos
                    ## e ajeita essa excessão de erro, caso não uma consulta errada crasha tudo
                    results = housing_crud.search_property(**args)
                    with col2:
                        show_results(atributes_apt, results, selected_atributes)  
                except pymysql.err.ProgrammingError:
                    st.write("Erro de consulta!")
                    ###########################################################################################################################################
        
        ## __Todo__!: Aqui você tem que mostrar todos os imóveis possíveis
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