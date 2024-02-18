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

    # Formato das infos: [estado/região, tipo de imóvel, tamanho, quantos quartos, quantos banheiros, Permite gatos, permite cachorros, Permite fumar?, acessível a cadeira de rodas, carregador para carros elétricos, vem mobiliado, latitude, longitude, preço ]
    new_apt = [None for _ in range(14)]

    housing_types = ["Apartamento", "Residência assistida", "Condomínio", "Cabine", "Duplex", "Flat", "Casa", "Anexo", "Terreno", "Loft","Manufaturado", "Casa de cidade" ]
    regions = ["reno / tahoe", "stockton" , "gainesville", "sarasota-bradenton", "macon / warner robin", "quad cities", "topeka", "rochester", "south jersey", "knoxville", "wichita"]
    col1, col2, col3 = st.columns([1,1,1])
    #Para perguntas de "Sim ou Não" serão usados os valores 0 e 1, referindo-se a não e sim respectivamente
    with col1:
        selected_housing =  st.selectbox("Qual o tipo de imóvel?", housing_types, index=0 )
        new_apt[1] = housing_types.index(selected_housing)
        new_apt[3] = st.number_input(f"Quantos quartos?", value=2, step=1, format="%d")
        new_apt[11] = st.number_input(f"Qual a latitude do imóvel?", value=39.5483)

    with col2:
        new_apt[2] = st.number_input(f"Qual o tamanho do imóvel? (SqFeet)", value= 750)
        new_apt[4] = st.number_input(f"Quantos banheiros?", value=3, step=1, format="%d")
        new_apt[12] = st.number_input(f"Qual a longitude do imóvel?", value=-119.746)

    with col3:
        new_apt[0] = st.selectbox(f"Qual a região/estado?", options= regions)
        new_apt[13] = st.number_input(f"Qual o preço do imóvel?", value= 1256.74)

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

        try:
            register_adress.register_adress(latitude = new_apt[11], longitude= new_apt[12], region=new_apt[0])
            create_region.create_region(region= new_apt[0],state= new_apt[0] )
            create_property.create_property(region = new_apt[0], price= new_apt[13], houseType= new_apt[1], sqfeet= new_apt[2], beds=new_apt[3], baths= new_apt[4], catsAllowed= new_apt[5], dogsAllowed = new_apt[6], smokingAllowed = new_apt[7], comesFurnished = new_apt[10], latitude = new_apt[11], longitude = new_apt[12])
            print(f" informações : {new_apt}")
        except pymysql.err.IntegrityError:
            print("Erro de integridade")


    #Aqui para nova região/Estado:

    st.write("<h4>Nova Região</h4>", unsafe_allow_html=True)
    st.markdown(f'''Selecione as características desejadas''')

    new_region = [None for _ in range(2)]
    cl1 , cl2, cl3= st.columns([3, 1.5, 3])

    with cl1:
        new_region[0] = st.text_input(f"Qual o nome do novo estado/região?")
    with cl2:
        new_region[1] = st.text_input(f"Qual a sigla do novo estado/região?")

    if st.button("Adicionar nova região"):
        regions.append(f"{new_region[0]} ({new_region[1]})")
        try:
            create_region.create_region(region= new_region[0], state= new_region[1])
            print(f" informações : {new_region}")
        except pymysql.err.IntegrityError:
            print("Erro de integridade")


create_add_menu()