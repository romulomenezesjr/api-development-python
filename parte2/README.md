# Entradas e saídas da API

Nesta etapa iremos criar estruturas padronizadas para entrada e saída de dados na API. Estas estruturas são essenciais para filtrar os dados necessários para o método chamado e retornar dados padronizados para um cliente utilizar.

A aplicação irá manipular métodos HTTP para responder as requisições conforme modelo REST. Os dados enviados serão armazenados na memória. 
# Objetivos
- [Estruturas (schemas) de entrada e saída dos dados](#estruturas-schemas-de-entrada-e-saída-dos-dados)
- [Armazenar dados em variável na memória](#armazenar-dados-em-variável-na-memória)
- [Requisições para API](#requisições-para-api)
- [Métodos Rest](#métodos-rest)
- [Acessando API](#acessando-api)

## Estruturas (schemas) de entrada e saída dos dados

As classes **ContentCreate** e **Content** que herdam do [BaseModel do pydantic](https://pydantic-docs.helpmanual.io/usage/schema/) são utilizadas pelo fastapi para transformar/validar dados provenientes do cliente **input** e retornar uma saída padronizada como **output**

## Armazenar dados em variável na memória
Os dados manipulados pela API são armazenados localmente em uma lista e são tratados pelos endpoints da API. 

## Requisições para API

A API aceita requisições que são enviadas por um cliente HTTP. As requisições são mapeadas para métodos normalmente são definidos com:  
- Tipo de requisição HTTP (GET/POST/PUT/DELETE)
- Caminho (Path)
- Dados de entrada (Request Model).
- Modelo de resposta (Response Model)
- Status de resposta (Response Status/Exceptions) 

## Métodos REST
- GET: Recuperar todos os conteúdos
    - Entrada: Nenhuma
    - Saída: List[Contents]
    - Status: 200
- GET: Recuperar 1 conteúdo
    - Entrada: id
    - Saída: Contents/None
    - Status: 200/404
- POST: Inserir 1 conteúdo
    - Entrada: ContentCreate
    - Saída: Contents
    - Status: 201
- PUT: Atualizar 1 conteúdo
    - Entrada: id, ContentCreate
    - Saída: Contents
    - Status: 200/404
- DELETE: Remover 1 conteúdo
    - Entrada: id
    - Saída: None
    - Status: 204/404

Status de respostas conforme [RFC](https://www.rfc-editor.org/rfc/rfc9110.html)

## Acessando API 
Para acessar a API com chamadas à todos os métodos podemos utilizar o openapi gerado automaticamente pelo fastapi. Para isso acessamos a url http://localhost:8001/docs
