# Parte 6 - Aplicando Casos de Uso, Autenticação e Configurações
Nesta etapa iremos adicionar configurações ao projeto e autenticação para usuários. Além disso iremos incluir regras para o uso dos endpoints e regras para permitir ou não requisições.

# Objetivos
- [Settings](#settings)
- [Autenticação](#autenticação)
- [Casos de uso](#casos-de-uso)

## Settings
- Configurações da descrição da API e do banco de dados armazenados em um arquivo .env e lidos no config/settings.py

## Autenticação

Instalar JOSE [Javascript Object Signing and Encription](#https://jose.readthedocs.io/en/latest/#javascript-object-signing-and-encryption-jose)

```bash
pip install jose
pip install python-jose
```

## Casos de Uso

### Endpoints abertos para acesso:

- Criar **Users**
- Recuperar informações de  **Playlists**  e seus respectivos **Contents**
- Recuperar informações de **Contents**

Autenticação é feita no endpoint /login. Os usuários autenticados recebem um token que expira em 30 minutos e devem enviar este para as requisições autenticadas.

### Endpoints para usuários autenticados:

Playlists

- Criar playlists 
- Atualizar         -> Usuário autenticado deve ser proprietário da playlist
- Apagar playlists  -> Usuário autenticado deve ser proprietário da playlist


Contents
- Criar 
- Atualizar -> Usuário autenticado deve ser proprietário da playlist do conteúdo
- Apagar    -> Usuário autenticado deve ser proprietário da playlist do conteúdo

Like 
- Playlist N x N Users
    - Um User pode favoritar (Like) em diversas Playlists
    - Uma Playlist pode ser favoritada por diversos Users