from abc import ABC
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.dao import DaoDB


class Repository(ABC):
    """Repository to make crud operations with specified dao"""

    def __init__(self, dao: DaoDB):
        self.dao = dao

    def get_all(self, db_session, skip: int = 0, limit: int = 10):
        """Returns all data from dao."""
        return self.dao.get_all(db_session, skip, limit)

    def get_by_id(self, model_id: int, db_session):
        """Returns a data with model_id from dao."""
        return self.dao.get_by_id(model_id, db_session)

    def save(self, schema, db_session):
        """Saves a schema data with dao."""
        return self.dao.save(schema, db_session)

    def update(self, model, schema, db_session):
        """Updates a model from a schema data with dao."""
        return self.dao.update(model, schema, db_session)

    def delete(self, model_data, db_session):
        """Deletes a model with dao."""
        self.dao.delete(model_data, db_session)


class ContentRepository(Repository):
    """Specific crud operations for contents table model."""


class PlaylistsRepository(Repository):
    """Specific crud operations for playlists table model."""

    def get_all_liked(self, db_session):
        """Returns all playlists from dao."""
        playlists = self.dao.get_all_liked(db_session)
        return playlists

    def get_liked(self, playlist_id, db_session):
        """Returns a playlists from dao."""
        playlist_local = self.dao.get_liked(playlist_id, db_session)
        return playlist_local

    def get_by_owner(self, playlist_id, user_id, db_session):
        """Returns a playlists from dao with specified id and user id."""
        playlist_local = self.dao.get_by_owner(playlist_id, user_id, db_session)
        return playlist_local


class UsersRepository(Repository):
    """Specific crud operations for user table model."""

    def get_by_email(self, email: EmailStr, db_session: Session):
        """Returns a user from dao with specified email."""
        return self.dao.get_user_by_email(email, db_session)
