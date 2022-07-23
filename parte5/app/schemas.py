from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Any, List, Optional, Union

## Content Schemas 
class ContentBase(BaseModel):
    title: str
    url: str
    playlist_id:int
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
    #created_at: datetime
    #playlist: Playlists
    class Config:
        orm_mode = True
        
# User
class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str]
class UserCreate(UserBase):
    password: str
    class Config:
        schema_extra = {
            "example": {
                "email": "romulo@gmail.com",
                "password": "remo",
                "name": "Romulo",
            }
        }
    
class User(UserBase):
    id: int    
    #created_at: datetime
    class Config:
        orm_mode = True

class UserDB(User):
    password: str


## Playlist Schemas 
class PlaylistBase(BaseModel):
    title: str
    thumbnail: str
    description: str
    published: bool
    user_id: int
    class Config:
        schema_extra = {
            "example": {
                "title": "Playlist ABC",
                "thumbnail": "https://www.spcdn.org/templates/sendpulsev1/img/sp_icons/sp-i-fb-autoposting.svg",
                "description": "Minha playlist",
                "published": True,
                "user_id": 1
            }
        }

class PlaylistCreate(PlaylistBase):
    pass

class Playlist(PlaylistBase):
    id: int
    #created_at: datetime
    user: User
    contents: List[Content]
    class Config:
        orm_mode = True



class LikedPlaylists(BaseModel):
    PlaylistModel: Playlist
    likes: int
    class Config:
        orm_mode = True