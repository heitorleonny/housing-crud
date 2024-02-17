import streamlit as st
import pandas as pd
import pymysql
import sqlalchemy as engine
#from database_setup.create_database import create_tables

st.set_page_config(
    page_title = "Implementação SQL - Rent Right",
    layout = "wide",
    menu_items = {
        'About': ''' Dashboard feito para visualização de manipulação do database Housing, feito por:
        \n- Alexandre Vital
        \n- Pedro Antunes
        \n- Vinícius Gomes
        \n- Vinícius Santos
        \n- Heitor Leony
        '''
    }
)

st.write("<h1>Banco de Dados Housing<h1>", unsafe_allow_html=True)
st.markdown('''
#### Bem vindo ao dashboard feito para visualização de manipulação do banco de dados Housing!
Aqui você pode visualizar estatísticas sobre o banco de dados Housing implementado em SQL algumas das funções disponíveis nesse dashboard incluem
            \n- Visualização das características do banco de dados
            \n- Operações de criação, leitura, atualização e remoção de elementos dentro do banco de dados (CRUD)
            
            ''')