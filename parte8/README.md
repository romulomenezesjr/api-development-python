# Parte 8 - Container na aplicação e deploy no digital ocean

Nesta etapa iremos colocar a aplicação em um container e fazer o deploy desta no Digital Ocean.

# Objetivos
- [Dockerfile](#dockerfile)
- [Docker-compose](#docker-composeyml)
- [Deploy na Digital Ocean](#digital-ocean)

## Dockerfile
Para construir uma imagem e iniciar um container utilizamos os comandos a seguir:
```bash
podman build -t api-python .
podman run -p 8000:8000 api-python
```

## docker-compose.yml
Para utilizamos um banco de dados mais robusto criamos um docker-compose.yml para criar um container de mysql e um container da aplicação automaticamente.
```bash
docker-compose up
```
Para o novo banco de dados necessitamos passar os dados de URL do banco no app/database.py e dados de acesso no .env

## Armazenando Imagem no docker-hub
```bash
podman image tag localhost/api-python docker.io/romulomenezes/fastapi-python
podman login docker.io
podman push docker.io/romulomenezes/fastapi-python
```

## Deploy na Digital Ocean

Criamos um droplet
- Image: Ubuntu 20.04
- Plan: Shared CPU
    - Regular 6$/M

Passos para copiar código e iniciar container
- SSH no IP do droplet para acessar a droplet
- Clonar repositório do git
- [Install docker on REPO](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt)
- Definir variáveis de ambiente (.env)
- docker-compose up -d
