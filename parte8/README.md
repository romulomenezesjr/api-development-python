# Parte 8 - Container na aplicação e deploy no digital ocean

Nesta etapa iremos colocar a aplicação em um container e fazer o deploy desta no digital ocean.


# Objetivos
- [Dockerfile](#dockerfile)
- [Docker-compose](#docker-composeyml)
- Digital Ocean
## Dockerfile
Para construir uma imagem e iniciar um container utilizamos os comandos a seguir:
```bash
podman build -t api-python .
podman run -p 8000:8000 api-python
```

## docker-compose.yml
Para utilizamos um banco de dados mais robusto criamos um docker-compose.yml para criar um container de mysql e um container da aplicação automaticamente.
Para o novo banco de dados necessitamos passar os dados de URL do banco no app/database.py e dados de acesso no .env



