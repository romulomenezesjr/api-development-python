from app.models import UserModel, PlaylistModel, LikedPlaylist
from sqlalchemy import func

class DaoDB:
    def __init__(self, Model):
        self.Model = Model

    def getAll(self, db, skip = 0, limit = 100):
        query = db.query(self.Model).offset(skip).limit(limit)
        models = query.all()
        return models

    def getById(self, id, db):
        return db.query(self.Model).filter(self.Model.id == id).first()
    
    def save(self, schema, db):
        db_model = self.Model(**schema.dict())
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        return db_model
    
    def update(self, local_model, schema, db):
        update_query = db.query(self.Model).filter(self.Model.id == local_model.id)
        update_query.update(schema.dict())

        db.commit()
        return update_query.first()
    
    def delete(self, local_model, db):
        db.delete(local_model)
        db.commit()

class Users_DB_Dao(DaoDB):
        
    def getUserByEmail(self, email, db):
        local_user = db.query(UserModel).filter(UserModel.email == email).first()
        return local_user
      
class Playlists_DB_Dao(DaoDB):

    def getAllLiked(self, db, skip = 0, limit = 100):
        query = db.query(
                            PlaylistModel, func.count(PlaylistModel.id).label("likes")
                        ).join(
                            LikedPlaylist, PlaylistModel.id == LikedPlaylist.playlist_id, isouter=True
                        ).group_by(
                            PlaylistModel.id
                        ).offset(skip).limit(limit)
        playlists_with_like = query.all()
        return playlists_with_like

    def getLiked(self, id, db):
        query = db.query(
                        PlaylistModel, func.count(PlaylistModel.id).label("likes")
                    ).join(
                        LikedPlaylist, PlaylistModel.id == LikedPlaylist.playlist_id, isouter=True
                    ).group_by(
                        PlaylistModel.id
                    ).filter(
                        PlaylistModel.id == id
                    )
        playlist_with_like = query.first()
        return playlist_with_like

    def getByOwner(self, playlist_id, user_id, db):
        return db.query(PlaylistModel).filter(PlaylistModel.user_id == user_id and PlaylistModel.id == playlist_id).first()

class Contents_DB_Dao(DaoDB):
    pass