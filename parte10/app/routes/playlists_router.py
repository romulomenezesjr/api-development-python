from typing import List
from fastapi import status, HTTPException, Response, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import LikedPlaylists, Playlist, PlaylistCreate, PlaylistDB
from app.utils import oauth2
from app.models import PlaylistModel, UserModel
from app.dao import Users_DB_Dao, Playlists_DB_Dao
from app.database import get_db
from app.repository import PlaylistsRepository, UsersRepository

playlistRepo = PlaylistsRepository(Playlists_DB_Dao(PlaylistModel))
userRepo = UsersRepository(Users_DB_Dao(UserModel))

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[LikedPlaylists])
def playlists(db_session: Session = Depends(get_db)):
    """
    GET ALL
    """
    return playlistRepo.get_all_liked(db_session)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=LikedPlaylists)
def get_playlist(playlist_id: int, db_session: Session = Depends(get_db)):
    """
    GET ID
    """
    playlist = playlistRepo.getLiked(playlist_id, db_session)
    if not playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Playlist with id {playlist_id} not found"
        )
    return playlist


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Playlist)
def create_playlist(
    playlist: PlaylistCreate,
    db_session: Session = Depends(get_db),
    user: UserModel = Depends(oauth2.get_current_user)
):
    """
    POST PLAYLIST
    """
    playlist_db = PlaylistDB(**playlist.dict(), user_id=user.id)
    new_playlist = playlistRepo.save(playlist_db, db_session)

    return new_playlist


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Playlist)
def update_playlist(
    playlist_id: int, playlist_input: PlaylistCreate,
    db_session: Session = Depends(get_db),
    user: UserModel = Depends(oauth2.get_current_user)
):
    """
    UPDATE PLAYLIST
    - Verifica se o id existe e lança 404 se não existe
    - Atualiza o conteúdo correspondente
    """
    local_playlist = playlistRepo.get_by_id(playlist_id, db_session)

    if not local_playlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Content with id {playlist_id} not found")

    if local_playlist.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"User {user.email} doest owns playlist {local_playlist.title}")

    updated_playlist = playlistRepo.update(local_playlist, playlist_input, db_session)

    return updated_playlist


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_playlist(
    playlist_id: int,
    db_session: Session = Depends(get_db),
    user: UserModel = Depends(oauth2.get_current_user)
):
    """
    DELETE PLAYLIST
    - Verifica se o id existe e lança 404 se não existe
    - Remove a playlist com id correspondente
    """
    local_playlist = playlistRepo.get_by_id(playlist_id, db_session)
    if not local_playlist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content with id {playlist_id} not found"
        )

    if local_playlist.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User {user.email} doest owns playlist {local_playlist.title}"
        )

    try:
        playlistRepo.delete(local_playlist, db_session)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{err.orig}"
        ) from err
