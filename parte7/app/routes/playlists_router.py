from threading import local
from typing import List
from fastapi import status, HTTPException,Response, APIRouter, Depends
from parte7.app.repository import PlaylistsRepository, UsersRepository
from sqlalchemy.orm import Session
from parte7.app.database import get_db
from parte7.app.schemas import  LikedPlaylists, Playlist, PlaylistCreate, PlaylistDB
from parte7.app.utils import oauth2
from parte7.app.models import PlaylistModel, UserModel
from parte7.app.dao import Users_DB_Dao, Playlists_DB_Dao

playlistRepo = PlaylistsRepository(Playlists_DB_Dao(PlaylistModel))
userRepo = UsersRepository(Users_DB_Dao(UserModel))

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
    responses={404: {"description": "Not found"}},
)

#@router.get("/", status_code = status.HTTP_200_OK, response_model = List[Playlists])
@router.get("/", status_code = status.HTTP_200_OK, response_model = List[LikedPlaylists])
def playlists(db: Session = Depends(get_db)):
    """
    GET ALL
    """
    return playlistRepo.getAllLiked(db)

@router.get("/{id}", status_code = status.HTTP_200_OK, response_model = LikedPlaylists)
def get_playlist(id: int, db: Session = Depends(get_db)):
    """
    GET ID
    """
    playlist = playlistRepo.getLiked(id, db)
    if not playlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist with id {id} not found" )
    return playlist

@router.post("/", status_code = status.HTTP_201_CREATED, response_model = Playlist)
def create_playlist(playlist: PlaylistCreate, db: Session = Depends(get_db), user:UserModel = Depends(oauth2.get_current_user)):
    """
    POST PLAYLIST
    """
    playlist_db = PlaylistDB(**playlist.dict(), user_id=user.id)
    new_playlist = playlistRepo.save(playlist_db, db)
    
    return new_playlist

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Playlist)
def update_playlist(id:int, playlist_input: PlaylistCreate, db: Session = Depends(get_db), user:UserModel = Depends(oauth2.get_current_user)):
    """
    UPDATE PLAYLIST
    - Verifica se o id existe e lança 404 se não existe
    - Atualiza o conteúdo correspondente
    """
    local_playlist = playlistRepo.getById(id, db)
    
    if not local_playlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )

    if local_playlist.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User {user.email} doest owns playlist {local_playlist.title}")
    
    updated_playlist = playlistRepo.update(local_playlist, playlist_input, db)
    
    return updated_playlist

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_playlist(id:int,db: Session = Depends(get_db), user:UserModel = Depends(oauth2.get_current_user)):
    """
    DELETE PLAYLIST
    - Verifica se o id existe e lança 404 se não existe
    - Remove a playlist com id correspondente
    """
    local_playlist = playlistRepo.getById(id, db)
    if not local_playlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    
    if local_playlist.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User {user.email} doest owns playlist {local_playlist.title}")
    
    try:
        playlistRepo.delete(local_playlist, db)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err.orig}")
