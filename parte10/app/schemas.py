from enum import Enum
from pydantic import BaseModel, EmailStr, conint
from typing import List, Optional

# Content Schemas


class ContentBase(BaseModel):
    title: str
    url: str
    playlist_id: int

    class Config:
        schema_extra = {
            "example": {
                "title": "Video XZY",
                "url": "https://www.youtube.com/watch?v=4AVdTQ196cQ",
                "playlist_id": 1,
            }
        }


class ContentCreate(ContentBase):
    pass


class Content(ContentBase):
    id: int
    # created_at: datetime
    # playlist: Playlists

    class Config:
        orm_mode = True

# OAuth


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

# User


class UserRoleIn(str, Enum):
    USER = "user"


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str]
    role: Optional[UserRole] = UserRole.USER


class UserCreate(UserBase):
    password: str
    role: Optional[UserRoleIn] = UserRoleIn.USER

    class Config:
        schema_extra = {
            "example": {
                "email": "romulo@gmail.com",
                "password": "remo",
                "name": "Romulo",
                "role": "user"
            }
        }


class UserUpdate(UserBase):
    password: str


class User(UserBase):
    id: int
    # created_at: datetime

    class Config:
        orm_mode = True


class UserDB(User):
    password: str


# Playlist Schemas
class PlaylistBase(BaseModel):
    title: str
    thumbnail: str
    description: str
    published: bool

    class Config:
        schema_extra = {
            "example": {
                "title": "Playlist ABC",
                "thumbnail": "xxxxxxxx",
                "description": "Minha playlist",
                "published": True
            }
        }


class PlaylistCreate(PlaylistBase):
    pass


class PlaylistDB(PlaylistBase):
    user_id: int


class Playlist(PlaylistDB):
    id: int
    # created_at: datetime
    user: User
    contents: List[Content]

    class Config:
        orm_mode = True


class LikedPlaylists(BaseModel):
    PlaylistModel: Playlist
    likes: int

    class Config:
        orm_mode = True


class Like(BaseModel):
    playlist_id: int
    user_id: int
    dir: conint(ge=0, le=1)
