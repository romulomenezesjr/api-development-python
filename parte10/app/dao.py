"""
This module contains classes responsible to persist and restore from database.
"""

from sqlalchemy import func
from app.models import UserModel, PlaylistModel, LikedPlaylist


class DaoDB:
    """
    Database CRUD operations
    """

    def __init__(self, model):
        """The model is used inside the methods to make a query."""
        self.model = model

    def get_all(self, db_session, skip=0, limit=100):
        """
        Returns all objects from the databse.
        """
        query = db_session.query(self.model).offset(skip).limit(limit)
        models = query.all()
        return models

    def get_by_id(self, object_id, db_session):
        """ Returns first row from the model table
            with the object_id especified.
        """
        return db_session.query(self.model).filter(
            self.model.id == object_id
        ).first()

    def save(self, schema, db_session):
        """Save the schema object in the database."""
        db_model = self.model(**schema.dict())
        db_session.add(db_model)
        db_session.commit()
        db_session.refresh(db_model)
        return db_model

    def update(self, local_model, schema, db_session):
        """Update the schema object in the database."""
        update_query = db_session.query(
            self.model
        ).filter(self.model.id == local_model.id)
        update_query.update(schema.dict())
        db_session.commit()
        return update_query.first()

    def delete(self, local_model, db_session):
        """Delete the schema object in the database."""
        db_session.delete(local_model)
        db_session.commit()


class Users_DB_Dao(DaoDB):
    """ Database CRUD operations for User table."""

    def get_user_by_email(self, email, db_session):
        """Returns first user with especified email from UserModel table."""
        local_user = db_session.query(UserModel).filter(
            UserModel.email == email
        ).first()
        return local_user


class Playlists_DB_Dao(DaoDB):
    """Database operations for Playlist table model."""

    def get_all_liked(self, db_session, skip=0, limit=100):
        """Returns playlists with like count."""
        query = db_session.query(
            PlaylistModel,
            func.count(PlaylistModel.id).label("likes")
        ).join(
            LikedPlaylist,
            PlaylistModel.id == LikedPlaylist.playlist_id,
            isouter=True
        ).group_by(
            PlaylistModel.id
        ).offset(skip).limit(limit)
        playlists_with_like = query.all()
        return playlists_with_like

    def get_liked(self, id, db_session):
        """Return the playlist with id and the like count."""
        query = db_session.query(
            PlaylistModel,
            func.count(PlaylistModel.id).label("likes")
        ).join(
            LikedPlaylist,
            PlaylistModel.id == LikedPlaylist.playlist_id,
            isouter=True
        ).group_by(
            PlaylistModel.id
        ).filter(
            PlaylistModel.id == id
        )
        playlist_with_like = query.first()
        return playlist_with_like

    def get_by_owner(self, playlist_id, user_id, db_session):
        """
            Returns the playlist with the especified
            id and from a especified user.
        """
        return db_session.query(
            PlaylistModel).filter(
            PlaylistModel.user_id == user_id and PlaylistModel.id == playlist_id
        ).first()


class Contents_DB_Dao(DaoDB):
    """Database operations for Contents table model."""
