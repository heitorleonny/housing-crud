import streamlit as st

def main():
    st.title("Seleção de Caixas de Texto")

    # Seletor para o número de caixas de texto
    num_caixas_texto = st.selectbox("Selecione o número de caixas de texto:", options=[1, 2, 3, 4, 5])

    # Lista para armazenar os textos das caixas de texto
    textos = []

    # Mostra as caixas de texto e armazena os textos
    for i in range(num_caixas_texto):
        texto = st.text_input(f"Caixa {i+1}", f"Digite o texto da caixa {i+1}")
        textos.append(texto)

    # Botão para exibir a lista de textos
    if st.button("Exibir Lista de Textos"):
        st.write("Lista gerada:")
        st.write(textos)

main()