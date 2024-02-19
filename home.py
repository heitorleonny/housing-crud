import streamlit as st

def main():
    st.set_page_config(
        page_title = "Implementação em MongoDB - Rent Right",
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
    Aqui você pode visualizar estatísticas sobre o banco de dados Housing implementado em MongoDB neste dashboard, você terá acesso a operações de criação, leitura, atualização e remoção de elementos dentro do banco de dados (CRUD)
                ''')

if __name__ == "__main__":
    main()