# Parte 5 - Realizar operações de CRUD para Contents, Playlists e Users
Nesta etapa iremos adicionar novas entidades à API: Playlists e Users. Estas entidades irão compor o sistema da seguinte forma:
- Cotents N x 1 Playlists
    - Um Content deverá estar associado à uma Playlist
    - Uma Playlist pode possuir diversos Contents
- Playlists N x 1 Users
    - Uma Playlist pertence à um User
    - Um User pode possuir diversas Playlists
- Users N x N Playlists
    - Um User pode dar Like em uma ou várias Playlists
    - Uma Playlist pode receber like de uma ou várias Playlists
# Objetivos
- [CRUD para Playlist](#crud-para-playlist-e-users)
- [CRUD para User](#crud-para-playlist-e-users)
- [CRUD para Like](#crud-para-playlist-e-users)

## CRUD para Playlist e Users
Para definirmos tabelas Playlists e um Users no banco de dados iremos definir um PlaylistModel e UserModel usando a classe Base do sqlalchemy. Este se encarregará de criar as tabelas ao iniciar, caso não existam. Também será necessário alterar a ContentModel para referenciar a tabela Playlists. 

Em seguida iremos definir os schemas para mapear entradas e saídas da API para Playlists e Users. Os módulos repository e dao iremos definir as operações de CRUD.
- Alterações em: Schema/Repository/DAO/Routes

Para usuários iremos criptografar o password com a biblioteca [passlib](https://passlib.readthedocs.io/en/stable/)
```bash
pip install passlib[bcrypt]
```