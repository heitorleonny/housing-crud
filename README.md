# Housing CRUD

## Instalando o Docker no Windows

Para instalar o Docker no Windows, você pode seguir as instruções detalhadas fornecidas na documentação oficial do Docker para Windows: [Instalando o Docker no Windows](https://docs.docker.com/desktop/install/windows-install/).

## Executando o Docker 

Para executar o banco de dados MongoDB usando Docker, você pode seguir estes passos:

```bash
docker run -d -p 27017:27017 --name mongo-container-2 vsgroot/rent-right-db
