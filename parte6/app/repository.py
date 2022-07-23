from abc import ABC
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.dao import DaoDB

class Repository(ABC):

    def __init__(self, dao: DaoDB):
        self.dao = dao

    def getAll(self, db, skip: int = 0, limit: int = 10):
        return self.dao.getAll(db, skip, limit)

    def getById(self, id: int, db):
        return self.dao.getById(id, db)

    def save(self, schema, db):
        return self.dao.save(schema, db)

    def update(self, model, schema, db):
        return self.dao.update(model, schema, db)

    def delete(self, model_data, db):
        self.dao.delete(model_data, db)

class ContentRepository(Repository):
    pass
class PlaylistsRepository(Repository):
    
    def getAllLiked(self, db):
        playlists = self.dao.getAllLiked(db)
        return playlists

    def getLiked(self, id, db):
        playlist_local = self.dao.getLiked(id, db)
        return playlist_local

    def getByOwner(self, playlist_id, user_id, db):
        playlist_local = self.dao.getByOwner(playlist_id, user_id, db)
        return playlist_local

class UsersRepository(Repository):
   
    def getByEmail(self, email: EmailStr, db:Session):
        return self.dao.getUserByEmail(email, db)

 