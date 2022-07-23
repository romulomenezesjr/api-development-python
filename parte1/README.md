# Parte 1: Criando ambiente para API REST
Nesta etapa iremos criar o ambiente para o projeto executar com o [virtual enviroment](https://docs.python.org/3/library/venv.html) e em seguida ativa-lo para instalar as bibliotecas necessárias para o projeto funcionar sem conflitos com bibliotecas de versões diferentes já instaladas no sistema. 
Em seguida, iremos utilizar no [arquivo principal](/app/main.py) a biblioteca fastapi e definir um endpoint para acessarmos. Para iniciar a API iremos utilizar o script [run.sh](run.sh) e acessar a url.

# Objetivos:
- [Criando um ambiente para implementação de API com fastapi](#criando-um-ambiente-para-implementação-de-api-com-fastapi)
- [Instalar bibliotecas necessárias](#instalar-bibliotecas-necessárias)
- [Arquivo Principal da API](#arquivo-principal-da-api)
- [Script para inicialização da API](#script-para-inicialização-da-api)
- [Execução do script de inicialização](#execução-do-script-de-inicialização)
- [Acessando API](#acessando-api)
- [Demonstração](#demonstração)

## Criando um ambiente para implementação de API com fastapi

Criando e ativiando o [virtual enviroment](https://docs.python.org/3/library/venv.html)

```
python3 -m venv venv
source venv/bin/activate

```

## Instalar bibliotecas necessárias
```bash
pip install fastapi[all]
pip install uvicorn[standard]
```

## Arquivo Principal da API

[app/main.py](./app/main.py)


## Script para inicialização da API
Arquivo [run.sh](run.sh)
## Execução do script de inicialização
```bash
chmod +x run.sh
./run.sh
```

## Acessando API 
http://localhost:8001

## Demonstração
http://localhost:8001


