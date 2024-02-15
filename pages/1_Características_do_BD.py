import streamlit as st

#Informações do BD:
itens_total = "NULL"
avg_price = "NULL"
avg_size = "NULL"

#Mostrar infos:

st.write("<h1>Características do Banco de dados</h1>", unsafe_allow_html=True)
st.markdown(f'''
Aqui você encontra algumas características do banco de dados que está sendo utilizado, as características apresentadas aqui serão atualizadas caso as características 
do Database mudem
        \n- Quantidade de apartamentos: {itens_total}
        \n- Média de preço dos apartamentos: {avg_price} USD 
        \n- Média de tamanho dos apartamentos: {avg_size}Ft
''')