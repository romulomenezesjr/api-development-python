# Objetivos
- [Migrations com Alembic](#migrations-com-alembic)
- CORS
- GIT
- HEROKU

## Migrations com Alembic
Iniciando o histórico de alterações no banco de dados com alembic

```bash
alembic init alembic
```

Arquivo alembic/env.py modificado para receber a classe Base.metadata e a string de conexão com o banco SQLALCHEMY_DATABASE_URL 
```python

context.config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

target_metadata = Base.metadata
```

alembic revision --autogenerate -m "Auto generate"
alembic upgrade fffffff


## CORS
Cross-Origin Resource Sharing (Compartilhamento de recursos com origens diferentes) é um mecanismo que usa cabeçalhos adicionais HTTP para informar a um navegador que permita que um aplicativo Web seja executado em uma origem (domínio) com permissão para acessar recursos selecionados de um servidor em uma origem distinta

O cors foi adicionado no main.py

## GIT
Criação do repositório no github
Criação do repositório localmente
```bash
git init 
git branch -M main
git add .
git commit -m "initial commit"
git add remote origin https://github.com/romulomenezesjr/api-development-python
git push

```
## Heroku
 

Install heroku
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install heroku --classic

Procfile
web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}

```bash
$ heroku login
$ heroku create my-api
```
Configure settings (.env) and mysql addon on heroku

```bash
$ git push heroku main
```


