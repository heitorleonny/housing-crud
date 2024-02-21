# Housing CRUD

## Instalando o Docker no Windows

Para instalar o Docker no Windows, você pode seguir as instruções detalhadas fornecidas na documentação oficial do Docker para Windows: [Instalando o Docker no Windows](https://docs.docker.com/desktop/install/windows-install/).

## Iniciando a aplicação

Para executar o banco de dados MongoDB usando Docker, você pode seguir estes passos:

1 - Instale o docker em sua máquina

2 - Faça um clone do repositório em sua máquina

3 - Realize a instalação dos requisitos executando o seguinte comando:
```bash
pip install -r requirements.txt
```
4 - No terminal, execute o seguinte comando para iniciar o docker:
```bash
docker run -d -p 27017:27017 --name mongo-container-2 vsgroot/rent-right-db
```
5 - Execute o streamlit através do seguinte comando:
```bash
streamlit run Home.py
```
