import streamlit as st
from database_setup import register_adress
from database_setup import create_property
from database_setup import create_region
import pymysql

#Ainda precisa fazer:
# Permitir atualização da pag de alguma forma (Talvez reescrevendo a pag?)
# Lista de possibilidades deve atalizar após adição de nova região

def create_add_menu():
    
    st.write("<h2>Adicionar dados</h2>", unsafe_allow_html=True)
    st.markdown(f'''Aqui você pode adicionar novos imóveis ou regiões no banco de dados, apenas insira os dados e depois aperte no botão para realizar a ação''')

    #Aqui para apartamentos:
    st.write("<h4>Novo imóvel</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

        #Formato usado:
    # 0: Nome da região
    # 1: Tipo de imóvel
    # 2: Tamanho do imóvel (SqFeet)
    # 3: Quantidade de quartos
    # 4: Quantidade de banheiros
    # 5: Permite gatos? (1 para sim, 0 para não)
    # 6: Permite cachorros? (1 para sim, 0 para não)
    # 7: Permite fumar? (1 para sim, 0 para não)
    # 8: Acessível a cadeira de rodas? (1 para sim, 0 para não)
    # 9: Possui carregador para carros elétricos? (1 para sim, 0 para não)
    # 10: Vem mobiliado? (1 para sim, 0 para não)
    # 11: Latitude do imóvel
    # 12: Longitude do imóvel
    # 13: Preço do imóvel
    # 14: Nome do estado
    
    
    new_apt = [None for _ in range(15)]

    housing_types = ["Apartamento", "Residência assistida", "Condomínio", "Cabine", "Duplex", "Flat", "Casa", "Anexo", "Terreno", "Loft","Manufaturado", "Casa de cidade" ]
    regions = ["reno / tahoe", "stockton" , "gainesville", "sarasota-bradenton", "macon / warner robin", "quad cities", "topeka", "rochester", "south jersey", "knoxville", "wichita"]
    col1, col2, col3 = st.columns([1,1,1])
    #Para perguntas de "Sim ou Não" serão usados os valores 0 e 1, referindo-se a não e sim respectivamente
    with col1:
        selected_housing =  st.selectbox("Qual o tipo de imóvel?", housing_types, index=0 )
        new_apt[1] = selected_housing
        new_apt[3] = st.number_input(f"Quantos quartos?", value=2, step=1, format="%d")
        new_apt[11] = st.number_input(f"Qual a latitude do imóvel?", value=39.5483)

    with col2:
        new_apt[2] = st.number_input(f"Qual o tamanho do imóvel? (SqFeet)", value= 750)
        new_apt[4] = st.number_input(f"Quantos banheiros?", value=3, step=1, format="%d")
        new_apt[12] = st.number_input(f"Qual a longitude do imóvel?", value=-119.746)

    with col3:
        new_apt[0] = st.number_input(f"Qual o nome da região?", value= 404)
        new_apt[13] = st.number_input(f"Qual o preço do imóvel?", value= 1256.74)
        new_apt[14] = st.number_input(f"Qual o nome do estado?", value= 405)

    col4, col5, col6 = st.columns([1,1,1])

    with col4:
        if st.toggle('Permite gatos?'):
            new_apt[5] = 1
        else:
            new_apt[5] = 0

        if st.toggle('Acessível a cadeira de rodas?'):
            new_apt[8] = 1
        else:
            new_apt[8] = 0

    with col5:
        if st.toggle('Permite cachorros?'):
            new_apt[6] = 1
        else:
            new_apt[6] = 0

        if st.toggle('Possui carregador para carros elétricos?'):
            new_apt[9] = 1
        else:
            new_apt[9] = 0

    with col6:
        if st.toggle('Permite fumar?'):
            new_apt[7] = 1
        else:
            new_apt[7] = 0

        if st.toggle('Vem mobiliado?'):
            new_apt[10] = 1
        else:
            new_apt[10] = 0    

    #Ainda precisa ser implementado:
# Formato das infos: [estado/região, tipo de imóvel, tamanho, quantos quartos, quantos banheiros, Permite gatos, permite cachorros, Permite fumar?, acessível a cadeira de rodas, carregador para carros elétricos, vem mobiliado, latitude, longitude, preço ]
    if st.button("Adicionar novo apartamento"):
        print(f" informações : {new_apt}")


        register_adress.register_adress(latitude = new_apt[11], longitude= new_apt[12], region=new_apt[0])
        create_region.create_region(region= new_apt[0],state= new_apt[0] )
        create_property.create_property(region = new_apt[0], price= new_apt[13], houseType= selected_housing, sqfeet= new_apt[2], beds=new_apt[3], baths= new_apt[4], catsAllowed= new_apt[5], dogsAllowed = new_apt[6], smokingAllowed = new_apt[7], comesFurnished = new_apt[10], latitude = new_apt[11], longitude = new_apt[12])
        print(f" informações : {new_apt}")
        print("Erro de integridade")


    #Aqui para nova região/Estado:

    st.write("<h4>Nova Região</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

    new_region = [None]
    cl1 , cl2, cl3= st.columns([3, 1.5, 3])

    with cl1:
        new_region[0] = st.text_input(f"Qual o nome do novo estado/região?")

    if st.button("Adicionar nova região"):
        try:
            create_region.create_region(region= new_region[0], state="")
            print(f" informações : {new_region}")
        except pymysql.err.IntegrityError:
            print("Erro de integridade")

    st.write("<h4>Novo Estado</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

    state = ["nome", "Abreviação"]
    col_1, col_2, col_3 = st.columns([1,1,5])

    with col_1:
        state[0] = st.text_input("Qual o nome do estado?")
    with col_2:
        state[1] = st.text_input("Qual a abreviação do estado?", max_chars=2)
    if st.button("Adicionar novo estado"):
        #Ainda precisa ser implementado
        print()

create_add_menu()
