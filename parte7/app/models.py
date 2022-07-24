from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Boolean, Text
from sqlalchemy.orm import relationship

#https://docs.sqlalchemy.org/en/14/core/type_basics.html

class LikedPlaylist(Base):
    __tablename__ = "liked_playlists"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade", onupdate="cascade"),primary_key=True )
    playlist_id = Column(Integer, ForeignKey("playlists.id", ondelete="cascade", onupdate="cascade"),primary_key=True )

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, unique=False)

    name = Column(String(255), nullable=True, unique=False)
    role = Column(String(255), nullable=True, unique=False, server_default="user")

    # created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) SQLite doest have now() method
    playlists = relationship("PlaylistModel", back_populates="user") 

    #liked_playlists = relationship("PlaylistModel", secondary=association_table,back_populates="liked_users")

    def __str__(self):
        return f"Email: {self.email}"

class PlaylistModel(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=False )
    description = Column(Text, index=False)
    thumbnail = Column(String(255), nullable=True, index=False )
    published = Column(Boolean, nullable=False, server_default="1")
    # created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) SQLite doest have now() method
    
    contents = relationship("ContentModel",back_populates="playlist")
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade", onupdate="cascade"), nullable=False)
    user = relationship("UserModel", back_populates="playlists")

    def __str__(self):
        return f"Id: {self.id}; Title: {self.title}; Owner: {self.user}"
    
class ContentModel(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=False )
    url = Column(String(255), index=False)
    # created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) SQLite doest have now() method
    playlist_id = Column(Integer, ForeignKey("playlists.id", ondelete="cascade", onupdate="cascade"), nullable=False)
    playlist = relationship("PlaylistModel", back_populates="contents")

