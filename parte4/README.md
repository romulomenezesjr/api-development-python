# Parte 4 - Utilizar Banco de Dados Relacionais

Nesta etapa configuramos o acesso ao banco de dados usando sqlite, realizamos a modelagem (criar tabelas) e a persistencia no banco de dados. Além disso, melhoramos a organização da rota para utilizar a classe APIRouter e inverter a dependência do route para a app.

# Objetivos

- [Instalar bibliotecas para acesso ao BD](#instalar-bibliotecas-para-acesso-ao-bd)
- [Configurar conexão](#configurar-conexão)
- [Definir modelos](#definir-modelos)
- [Atualizar schemas](#atualizar-schemas)
- [Atualizar o repository](#atualizar-o-repository)
- [Atualizar routes](#atualizar-routes)

## Instalar bibliotecas para acesso ao BD
Para conexão com banco de dados mysql é necessário instalar o sqlalchemy e o pymysql (MySQL). Após isso configurar a url de conexão no arquivo database.py que informa o usuário, senha, host, porta e nome do banco de dados.
Caso o banco de dados seja o sqlite basta instalar o sqlalchemy.

```bash
pip install sqlalchemy
pip install pymysql
```

## Configurar conexão
Conexão é iniciada no arquivo database.py onde são passados os parâmetros de conexão e é criada a sessão. A Base class e um método get_db são usados por outras partes da API

## Definir modelos

Os modelos são utilizados para criar as tabelas, mapear classe para tabela e realizar operações. 
[Ref](https://docs.sqlalchemy.org/en/14/core/type_basics.html)

## Atualizar schemas
Os schemas foram atualizados para haver compatibilidade de atributos entre o modelo do sqlalchemy e do pydantic.


## Atualizar o repository

O repository irá utilizar o contents_db_dao e este por sua vez irá persistir os dados com o orm sqlalchemy. 


## Atualizar routes
O módulo routes foi atualizado para incluir a classe APIRouter realizar a inversão de dependência. Anteriormente o routes necessitava da app. Agora a app inclui um routes e poderá incluir outros daqui em diante 