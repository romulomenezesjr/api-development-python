from typing import List
from fastapi import status, HTTPException,Response, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import PlaylistCreate, Playlist,LikedPlaylists
from app.repository import PlaylistsRepository
from app.dao import Playlists_DB_Dao
from app.models import PlaylistModel
from app.database import get_db

playlistRepo = PlaylistsRepository(Playlists_DB_Dao(PlaylistModel))

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", status_code = status.HTTP_200_OK, response_model = List[LikedPlaylists])
def playlists(db: Session = Depends(get_db)):
    """
    GET ALL
    """
    playlists = playlistRepo.getAllLiked(db)
    return playlists

@router.get("/{id}", status_code = status.HTTP_200_OK, response_model = LikedPlaylists)
def get_playlist(id: int, db: Session = Depends(get_db)):
    """
    GET ID
    """
    content = playlistRepo.getById(id, db)
    if not content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Playlist with id {id} not found" )
    return content

@router.post("/", status_code = status.HTTP_201_CREATED, response_model = Playlist)
def create_playlist(playlist: PlaylistCreate, db = Depends(get_db)):
    """
    POST A PLAYLIST
    """
    new_playlist = playlistRepo.save(playlist, db)

    if new_playlist is None:
        raise HTTPException(status_code=400)
    
    return new_playlist

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Playlist)
def update_content(id:int, content: PlaylistCreate, db: Session = Depends(get_db)):
    """
    UPDATE PLAYLIST
    - Verifica se o id existe e lança 404 se não existe
    - Atualiza o conteúdo correspondente
    """
    local_content = playlistRepo.getById(id, db)
    if not local_content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    updated_content = playlistRepo.update(local_content, content, db)
    return updated_content

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_playlist(id:int, db: Session = Depends(get_db)):
    """
    DELETE PLAYLIST
    - Verifica se o id existe e lança 404 se não existe
    - Remove a playlist com id correspondente
    """
    local_playlist = playlistRepo.getById(id, db)
    if not local_playlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    playlistRepo.delete(local_playlist, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

