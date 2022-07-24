from typing import List
from fastapi import status, HTTPException, APIRouter, Depends
from app.repository import PlaylistsRepository, UsersRepository
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import  Like
from app.utils import oauth2
from app.models import LikedPlaylist, PlaylistModel, UserModel
from app.dao import Playlists_DB_Dao, Users_DB_Dao

playlistRepo = PlaylistsRepository(Playlists_DB_Dao(PlaylistModel))
userRepo = UsersRepository(Users_DB_Dao(UserModel))

router = APIRouter(
    prefix="/likes",
    tags=["likes"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=status.HTTP_200_OK)
def like_playlist(like_body: Like, db: Session = Depends(get_db), user = Depends(oauth2.get_current_user)):
    
    local_playlist = playlistRepo.getById(like_body.playlist_id, db)
    
    print(f"user {user} liked {local_playlist}")
    
    like_query = db.query(LikedPlaylist).filter(LikedPlaylist.playlist_id == like_body.playlist_id , LikedPlaylist.user_id == user.id)

    like = like_query.first()

    if like is None:
        new_like = LikedPlaylist(playlist_id=like_body.playlist_id, user_id=user.id)
        db.add(new_like)
        db.commit()
        return {"message": "sucessfully liked"}
    
    if like_body.dir == 1:
        raise HTTPException(status.HTTP_409_CONFLICT)
    else:        
        like_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "sucessfully unliked"}
    
