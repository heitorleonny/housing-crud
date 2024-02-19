import streamlit as st
import pymongo
from mongoDB import mongoDB
import pymysql

#Ainda precisa fazer:
# Permitir atualização da pag de alguma forma (Talvez reescrevendo a pag?)
# Lista de possibilidades deve atalizar após adição de nova região

def create_add_menu():
    #Reajustar isso depois
    
    st.write("<h2>Adicionar dados</h2>", unsafe_allow_html=True)
    st.markdown(f'''Aqui você pode adicionar novos imóveis ou regiões no banco de dados, apenas insira os dados e depois aperte no botão para realizar a ação''')

    #Aqui para apartamentos:
    st.write("<h4>Novo imóvel</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

    # Formato das infos: [estado/região, tipo de imóvel, tamanho, quantos quartos, quantos banheiros, Permite gatos, permite cachorros, Permite fumar?, acessível a cadeira de rodas, carregador para carros elétricos, vem mobiliado, latitude, longitude, preço ]
    new_apt = {}

    housing_types = [ "Casa", "Apartamento", "Condomínio" ]
    regions = [ "Norte", "Sul", "Leste", "Oeste"]
    states = [ "Casa", "Apartamento", "Condomínio" ]
    
    new_apt['desc'] = st.text_area(f"Qual a descrição do imóvel?")
    
    col1, col2, col3 = st.columns([1,1,1])
    #Para perguntas de "Sim ou Não" serão usados os valores 0 e 1, referindo-se a não e sim respectivamente
    with col1:
        new_apt['type'] =  st.selectbox("Qual o tipo de imóvel?", housing_types, index=0 )
        new_apt['region'] = st.selectbox(f"Qual a região?", options= regions)
        new_apt['beds'] = st.number_input(f"Quantos quartos?", value=2, step=1, format="%d")
        new_apt['lat'] = st.number_input(f"Qual a latitude do imóvel?", value=39.5483)

    with col2:
        new_apt['state'] =  st.selectbox("Qual o estado?", states, index=0 )
        new_apt['baths'] = st.number_input(f"Quantos banheiros?", value=3, step=1, format="%d")
        new_apt['long'] = st.number_input(f"Qual a longitude do imóvel?", value=-119.746)

    with col3:
        new_apt['price'] = st.number_input(f"Qual o preço do imóvel?", value= 1256.74)
        new_apt['sqfeet'] = st.number_input(f"Qual o tamanho do imóvel? (SqFeet)", value= 750)

    col4, col5, col6 = st.columns([1,1,1])

    with col4:
        new_apt['cats_allowed'] = st.toggle('Permite gatos?')
        new_apt['comes_furnished'] = st.toggle('Vem mobiliado?') 


    with col5:
        new_apt['dogs_allowed'] = st.toggle('Permite cachorros?')

    with col6:
        new_apt['smoking_allowed'] = st.toggle('Permite fumar?')

# Formato das infos: [estado/região, tipo de imóvel, tamanho, quantos quartos, quantos banheiros, Permite gatos, permite cachorros, Permite fumar?, acessível a cadeira de rodas, carregador para carros elétricos, vem mobiliado, latitude, longitude, preço ]
    if st.button("Adicionar novo apartamento"):
        print(f" informações : {new_apt}")
        mongoDB.MongoDBManager.insert_document({
            'region':new_apt['region'],
            'price': new_apt['price'], 
            'houseType': new_apt['type'], 
            'sqFeet': new_apt['sqfeet'], 
            'beds': new_apt['beds'], 
            'baths': new_apt['baths'], 
            'catsAllowed': new_apt['cats_allowed'], 
            'dogsAllowed':new_apt['dogs_allowed'], 
            'smokingAllowed':new_apt['smoking_allowed'], 
            'comesFurnished':new_apt['comes_furnished'], 
            'latitude': new_apt['lat'], 
            'longitude': new_apt['long'],
            'state':new_apt['state']
            })


create_add_menu()