# Configuração da aplicação
Atenção: é necessário ter o Python e o MYSQL instalados na máquina para seguir o passo a passo

## 1-Faça um clone do repositório
`git clone https://github.com/heitorleonny/housing-crud.git`

## 2-Mude para a branch sql-implementation
se estiver utilizando o terminal use o comando `git checkout sql-implementation`

## 3-Crie um ambiente virtual
Abra o projeto em uma IDE(indicamos VSCode) e abra um terminal para executar o comando `python -m venv env`

## 4-Ative o ambiente virtual
`.\env\Scripts\activate`

## 5-Instale as dependências
`pip install -r requirements.txt`

## 6-Insira seu usuário e senha do Workbanch em database_setup/config.cfg
![image](https://github.com/heitorleonny/housing-crud/assets/108541219/bf4fe206-c157-41c6-83b8-077e8969c527)

## 7-Rode a aplicação Streamlit
`streamlit run home.py`

## 8-Aproveite
Prontinho, agora o stramlit vai abrir uma página no seu navegar e você poderá testar a aplicação!
