# Parte 3 - Organizar Arquitetura da API e Documentar

Nesta etapa iremos separar as responsabilidades da API em módulos diferentes. Um módulo de rotas para atender um caminho específico, um módulo de repositório para abstrair o acesso aos dados, um módulo de dao que implementa o acesso aos dados e, por fim, um módulo para schemas que estabelece o modelo de entrada e saída de dados e é utilizado na documentação.

## Objetivos
- [Routes](#routes)
- [Repository](#repository)
- [DAO](#dao)
- [Documentar a API](#documentar-a-api)
- [Schemas](#schemas)

## Routes
O módulo routes foi utilizado para organizar em arquivos específicos as requisições HTTP para o caminho /contents

## Repository
O módulo repository foi utilizado para trabalhar o acesso aos dados. A classe abstrata Repository possui os métodos abstratos a seguir que são implementados pelo ContentsRepository. Este, por sua vez, faz acesso direto aos dados (DAO) utilizando o dao/contents_memory_dao.py. 

- get()         -> Retorna todos
- get(id)       -> Retorna o elemento pelo id
- save(e)       -> Salva o elemento
- update(e, n)  -> Atualiza o elemento e com os dados em new_e
- delete(id)    -> Remove o elemento com id e

## DAO
O DAO faz o acesso direto aos dados. Neste momento o acesso é feito na memória, na próxima etapa fazer o acesso ao banco de dados sqlite ou mysql. 

## Schemas
O módulo schemas foi utilizado para organizar a representação dos dados de entrada e saída da API

## Documentar a API
Inserir documentação no arquivo main.py e nos schemas para serem utilizados pela documentação da api gerada automaticamente pelo fastapi/swagger