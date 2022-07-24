# API com Python/FastAPI/MySQL

Neste repositório buscamos demonstrar o desenvolvimento de uma API em 10 etapas.  Desde a criação do ambiente, passando por crud/métodos rest, casos banco de dados, casos de uso, autenticação, migrations, testes e integração contínua. O propósito da separação em progressiva em partes é educacional. 

# Tabela de conteúdos 
   * [Sobre API]()
   * [Tecnologias](#Tecnologias)
   * [Etapas](#Etapas)
        * [Parte 1: Criando ambiente e acessando a API](#parte-1-criando-ambiente-e-acessando-a-api)
        * [Parte 2: Entradas e Saídas da API](#parte-2) 
# Sobre a API

A API irá fornecer dados para uma aplicação controlar dados de playlists pertencentes à usuários e seus respectivos conteúdos. 

# 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [uvicorn](https://www.uvicorn.org/)
- [python-jose](https://pypi.org/project/python-jose/camada)

# Etapas
## Parte 1: Criando ambiente e acessando a API
- [Parte 1: Criando ambiente para API REST](parte1/README.md#criando-um-ambiente-para-implementação-de-api-com-fastapi)
- [Instalar bibliotecas necessárias](parte1/README.md#instalar-bibliotecas-necessárias)
- [Arquivo Principal da API](parte1/README.md#arquivo-principal-da-api)
- [Script para inicialização da API](parte1/README.md#script-para-inicialização-da-api)
- [Execução do script de inicialização](parte1/README.md#execução-do-script-de-inicialização)
- [Acessando API](parte1/README.md#acessando-api)
- [Demonstração](parte1/README.md#demonstração)

- Propostas de Estudo:
    - Frameworks para desenvolvimento de API rest em Python: fastapi/django-rest/flask
    - Tecnologias utilizadas para API REST: Java-Spring/Node-Express/Python-fastapi/PHP-Laravel/Go-?

## Parte 2 - Entradas e saídas da API
- [Estruturas (schemas) de entrada e saída dos dados](parte2/README.md#estruturas-schemas-de-entrada-e-saída-dos-dados)
- [Armazenar dados em variável na memória](parte2/README.md#armazenar-dados-em-variável-na-memória)
- [Requisições para API](parte2/README.md#requisições-para-api)
- [Métodos Rest](parte2/README.md#métodos-rest)
- Propostas de Estudo:
    - Testes automatizados em API 
    - Comparação entre estratégias de troca de dados (REST/SOAP/GraphSQL/gRPC)

## Parte 3 - Organizar Arquitetura da API e Documentar
## Objetivos
- [Routes](parte3/README.md#routes)
- [Repository](parte3/README.md#repository)
- [DAO](parte3/README.md#dao)
- [Documentar a API](parte3/README.md#documentar-a-api)
- [Schemas](parte3/README.md#schemas)
- Propostas de Estudo
    - Ferramentas para documentação de API
    - Arquiteturas para aplicações: MVC/Arquitetura Clean/

## Parte 4 - Utilizar Banco de Dados Relacionais
## Objetivos
- [Instalar bibliotecas para acesso ao BD](parte4/README.md#instalar-bibliotecas-para-acesso-ao-bd)
- [Configurar conexão](parte4/README.md#configurar-conexão)
- [Definir modelos](parte4/README.md#definir-modelos)
- [Atualizar schemas](parte4/README.md#atualizar-schemas)
- [Atualizar o repository](parte4/README.md#atualizar-o-repository)
- [Atualizar routes](parte4/README.md#atualizar-routes)
- Propostas de Estudo
    - Vantagens/Desvantagens entre tipos de banco de dados: Relacionais/Não Relacionais
    - Comparação entre arquiteturas para aplicações: DDD/Arquitetura Clean/Hexagonal/
## Parte 5 - Realizar operações de CRUD para Contents, Playlists e Users
## Objetivos
- [CRUD para Playlist](#crud-para-playlist-e-users)
- [CRUD para User](#crud-para-playlist-e-users)
- [CRUD para Like](#crud-para-playlist-e-users)
- Propostas de Estudo
    - Normalização em Bancos de Dados
    - Recomendação com base em relacionamentos