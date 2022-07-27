from fastapi import status, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.repository import PlaylistsRepository, UsersRepository
from app.database import get_db
from app.schemas import Like
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
def like_playlist(like_body: Like, db_session: Session = Depends(get_db), user=Depends(oauth2.get_current_user)):

    local_playlist = playlistRepo.get_by_id(like_body.playlist_id, db_session)

    print(f"user {user} liked {local_playlist}")

    like_query = db_session.query(LikedPlaylist).filter(
        LikedPlaylist.playlist_id == like_body.playlist_id,
        LikedPlaylist.user_id == user.id
    )

    like = like_query.first()

    if like is None:
        new_like = LikedPlaylist(playlist_id=like_body.playlist_id, user_id=user.id)
        db_session.add(new_like)
        db_session.commit()
        return {"message": "sucessfully liked"}

    if like_body.dir == 1:
        raise HTTPException(status.HTTP_409_CONFLICT)

    like_query.delete(synchronize_session=False)
    db_session.commit()
    return {"message": "sucessfully unliked"}
