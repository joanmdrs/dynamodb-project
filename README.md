# Aplicação desenvolvida utilizando o DynamoDB

<img width=400 src="https://miro.medium.com/max/700/1*cmfoGi3FnVIBCwvmVLYgjg.png" />

## Sobre o projeto
Este projeto foi desenvolvido durante o curso da disciplina Projeto e Administração de Banco de Dados, ministrada pelo professor Taciano 
no curso de Bacharelado em Sistemas da Informação, pela Universidade Federal do Rio Grande do Norte / CERES - Caicó/RN. 

## Desenvolvedores 

* [Adson Santos](https://github.com/adson-matheus)
* [Allan Almeida](https://github.com/allangbr)
* [Joan Medeiros](https://github.com/joanmdrs)
* [Rauan Meirelles](https://github.com/rauan-meirelles)
* [Wesley Morais](https://github.com/WesleyVitor)

## Tecnologias utilizadas 

* ![Python](https://img.shields.io/badge/Python-3e7aaa?style=for-the-badge&logo=python&logoColor=white)
* ![DynamoDB](https://img.shields.io/badge/DynamoDB-1a476f?&style=for-the-badge&logo=amazonaws&logoColor=white)
* ![PynamoDB](https://img.shields.io/badge/PynamoDB-4F4F4F?&style=for-the-badge&logo=orm&logoColor=white)
* ![FasTAPI](https://img.shields.io/badge/FastAPI-009586?style=for-the-badge&logo=fastapi&logoColor=white)
* ![Uvicorn](https://img.shields.io/badge/Uvicorn-4051b5?&style=for-the-badge&logo=uvicorn&logoColor=white)

## Dependência

* ![Python](https://img.shields.io/badge/Python-3e7aaa?style=for-the-badge&logo=python&logoColor=white)
* ![Docker](https://img.shields.io/badge/Docker-2496ed?style=for-the-badge&logo=docker&logoColor=white)


## Instalação

Nesta seção você encontra o tutorial de execução do projeto

### Clonando o projeto

```console
git clone https://github.com/joanmdrs/dynamodb-project.git
```

### Criando o container do DynamoDB para rodar localmente

```console
docker run -d -p 8000:8000 --name dynamodb-server amazon/dynamodb-local
```

### Instalando o AWS-CLI

```console
pip install awscli
```

### Configurando credenciais fictícias 

```console
aws configure
```
Após digitar esse comando, insira as seguintes informações:

- Para AWS Access Key ID, insira:
```console 
fakeMyKeyId
```

- Para AWS Secret Access Key, insira:
```console 
fakeSecretAccessKey
```

-  Para Default region name, insira:
```console 
us-west-2
```

- Para Default output format, insira:
```console 
json
```

### Visualize tabelas locais do DynamoDB com a GUI de administração do DyanmoDB

```console 
npm install -g dynamodb-admin
```

```console 
DYNAMO_ENDPOINT=http://localhost:8000/ dynamodb-admin

```

### Rodando a aplicação do FastAPI

- Entre na pasta do repositório: 

 
```console
cd dynamodb-project
```

- Crie o ambiente virtual 


```console
python -m venv venv
```
- Ative o ambiente virtual


```console
source venv/bin/activate
```
- Instale as dependências:

```console
pip install -r requirements.txt
```

- Execute a aplicação 

```console
uvicorn main:app --reload
```
- Acesse o domínio

```console
localhost:8002
```




