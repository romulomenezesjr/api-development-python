# Objetivos
- Migrations com Alembic
- CORS
- GIT
- HEROKU

## Alembic
Iniciando o histórico de alterações no banco de dados com alembic

```bash
alembic init alembic
```

Arquivo alembic/env.py modificado para receber a classe Base.metadata e a string de conexão com o banco SQLALCHEMY_DATABASE_URL 
```python
from alembic import context
context.config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

target_metadata = Base.metadata
```

alembic revision --autogenerate -m "Auto generate"
alembic upgrade fffffff


## CORS


## GIT

## Heroku
 

Install heroku
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install heroku --classic

Procfile
web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}

```bash
$ heroku login
$ heroku create plym-api
```
Configure settings (.env) and mysql addon on heroku

```bash
$ git push heroku main
```


