from typing import List
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Response, APIRouter, Depends
from app.database import get_db
from app.schemas import ContentCreate, Content
from app.repository import ContentRepository, PlaylistsRepository
from app.utils import oauth2
from app.dao import Contents_DB_Dao, Playlists_DB_Dao
from app.models import ContentModel, PlaylistModel

contents_repo = ContentRepository(Contents_DB_Dao(ContentModel))
playlists_repo = PlaylistsRepository(Playlists_DB_Dao(PlaylistModel))

router = APIRouter(
    prefix="/contents",
    tags=["contents"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Content])
def contents(db_session: Session = Depends(get_db), skip: int = 0, limit: int = 5):
    """
    GET ALL
    """
    limit = limit if limit < 100 else 100
    return contents_repo.get_all(db_session, skip, limit)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Content)
def get_content(content_id: int, db_session: Session = Depends(get_db)):
    """
    GET ID
    """
    content = contents_repo.get_by_id(content_id, db_session)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content with id {content_id} not found"
        )
    return content


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Content)
def create_content(content: ContentCreate, db_session: Session = Depends(get_db), user=Depends(oauth2.get_current_user)):
    """
    POST CONTENT
    """
    local_playlist = playlists_repo.getByOwner(content.playlist_id, user.id, db_session)

    if local_playlist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Playlist with id {id} not found"
        )

    if local_playlist.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User {user.email} doest owns playlist {local_playlist.title}"
        )

    new_content = contents_repo.save(content, db_session)

    return new_content


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Content)
def update_content(
    content_id: int,
    content: ContentCreate,
    db_session: Session = Depends(get_db),
    user=Depends(oauth2.get_current_user)
):
    """
    UPDATE CONTENT
    - Verifica se o id existe e lança 404 se não existe
    - Atualiza o conteúdo correspondente
    """
    local_playlist = playlists_repo.get_by_owner(content.playlist_id, user.id, db_session)

    if local_playlist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Playlist with id {content_id} not found"
        )

    if local_playlist.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User {user.email} doest owns playlist {local_playlist.title}"
        )

    local_content = contents_repo.get_by_id(content_id, db_session)

    if not local_content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content with id {content_id} not found"
        )

    updated_content = contents_repo.update(local_content, content, db_session)
    return updated_content


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_content(content_id: int, db: Session = Depends(get_db), user=Depends(oauth2.get_current_user)):
    """
    DELETE CONTENT
    - Verifica se o id existe e lança 404 se não existe
    - Remove o conteúdo com id correspondente
    """

    local_content = contents_repo.get_by_id(content_id, db)
    if not local_content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {content_id} not found")

    playlist_local = playlists_repo.get_by_id(local_content.playlist_id, db)
    if playlist_local.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail=f"User doest owns Content Playlist with id {playlist_local.id}")

    contents_repo.delete(local_content, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
