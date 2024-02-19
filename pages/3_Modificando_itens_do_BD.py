import streamlit as st


def create_search_menu(table):
    st.write(f"<h3>Item escolhido: {table}<h3>", unsafe_allow_html=True)
    cl1, cl2 = st.columns([1,3])

    if table == "Imóveis":
        with cl1:
            id = st.number_input(f"Insira o ID do imóvel", value=000)
        create_property_menu(id)
    elif table == "Estados":
        with cl1:
            id = st.text_input(f"Insira o ID do estado", value=000)
        create_state_menu(id)
    elif table == "Regiões":
        with cl1:
            id = st.number_input(f"Insira o ID da região", value=000)
        create_region_menu(id)

        

def create_region_menu(id):
    #Implementar com código real depois:
    name = "popopipiska" #placeholder
    regstate_infos = [ id , name]

    col1, col2, col3 = st.columns([1,1,2])
    with col1:
        ID_show = st.text_input(f"ID", value=id, disabled=True)
        if st.button("Editar"):
            print("Saving modifications...")
            #Falta o código
            with col3:
                st.write("Modificações salvas!")
    with col2:
        new_name = st.text_input(f"Nome", value=name)
        if st.button("Deletar elemento"):
            print("Deletando elemento...")
            #Falta código
            with col3:
                st.write("item removido!")

def create_property_menu(id):
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
    current_props = ['stockton', "Cabine", 115, 2, 3, 1, 1, 1, 1, 1, 1, 39.5483, -119.746, 935.0, "Texas"]

    housing_types = ["Apartamento", "Residência assistida", "Condomínio", "Cabine", "Duplex", "Flat", "Casa", "Anexo", "Terreno", "Loft","Manufaturado", "Casa de cidade" ]
    #Ajeitar depois
    regions = ["reno / tahoe", "stockton" , "gainesville", "sarasota-bradenton", "macon / warner robin", "quad cities", "topeka", "rochester", "south jersey", "knoxville", "wichita"]
    states = ['ny', 'etc']
    
    col1, col2, col3 = st.columns([1,1,1])
    #Para perguntas de "Sim ou Não" serão usados os valores 0 e 1, referindo-se a não e sim respectivamente
    with col1:
        id_show = st.text_input(f"ID", value=id, disabled=True)
        new_apt[3] = st.number_input(f"Quantos quartos?", value=current_props[3], step=1, format="%d")
        new_apt[11] = st.number_input(f"Qual a latitude do imóvel?", value=current_props[11])
        new_apt[14] = st.number_input(f"Qual o nome do estado?", value= 405)

    with col2:
        new_apt[1] =  st.selectbox("Qual o tipo de imóvel?", housing_types, index= housing_types.index(current_props[1]))
        new_apt[4] = st.number_input(f"Quantos banheiros?", value=current_props[4], step=1, format="%d")
        new_apt[12] = st.number_input(f"Qual a longitude do imóvel?", value=current_props[12])

    with col3:
        new_apt[2] = st.number_input(f"Qual o tamanho do imóvel? (SqFeet)", value= current_props[2])
        new_apt[0] = st.number_input(f"Qual o nome da região?", value= 404)
        new_apt[13] = st.number_input(f"Qual o preço do imóvel?", value=current_props[13])

    col4, col5, col6 = st.columns([1,1,1])

    with col4:
        if st.toggle('Permite gatos?', value=true_or_false(current_props[5])):
            new_apt[5] = 1
        else:
            new_apt[5] = 0

        if st.toggle('Acessível a cadeira de rodas?',value=true_or_false(current_props[8])):
            new_apt[8] = 1
        else:
            new_apt[8] = 0

    with col5:
        if st.toggle('Permite cachorros?', value=true_or_false(current_props[5])):
            new_apt[6] = 1
        else:
            new_apt[6] = 0

        if st.toggle('Possui carregador para carros elétricos?', value=true_or_false(current_props[9])):
            new_apt[9] = 1
        else:
            new_apt[9] = 0

    with col6:
        if st.toggle('Permite fumar?', value=true_or_false(current_props[7])):
            new_apt[7] = 1
        else:
            new_apt[7] = 0

        if st.toggle('Vem mobiliado?', value=true_or_false(current_props[10])):
            new_apt[10] = 1
        else:
            new_apt[10] = 0

    colum_1, colum_2, colum_3 = st.columns([1,1,7])
    with colum_1:
        if st.button("Editar"):
            print("Saving modifications...")
            #Falta o código
            with colum_3:
                st.write("Modificações salvas!")
    with colum_2:
        if st.button("Deletar elemento"):
            print("Deletando elemento...")
            #Falta código
            with colum_3:
                st.write("item removido!")

def create_state_menu(id):
    #Implementar com código real depois:
    name = "popopipiska" #placeholder
    abrev = "po"
    regstate_infos = [ id , name, abrev]

    col1, col2, col3, col4 = st.columns([1,1,0.5,2])
    with col1:
        ID_show = st.text_input(f"ID", value=id, disabled=True)
        if st.button("Editar"):
            print("Saving modifications...")
            #Falta o código
            with col3:
                st.write("Modificações salvas!")
    with col2:
        new_name = st.text_input(f"Nome", value=name)
        if st.button("Deletar elemento"):
            print("Deletando elemento...")
            #Falta código
            with col3:
                st.write("item removido!")
    with col3:
        new_abrev = st.text_input(f"Sigla", value=abrev, max_chars=2)

def true_or_false(value):
    if value == 0:
        return False
    elif value == 1:
        return True
    return None
st.write("<h2>Modificando itens do BD<h2>", unsafe_allow_html=True)
st.markdown(f'''Aqui você pode modificar ou deletar itens presentes em seu banco de dados''')
selected_table = st.selectbox("Qual tipo de item você quer modificar?", ("Imóveis", "Estados", "Regiões" ))
create_search_menu(selected_table)