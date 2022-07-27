from typing import List
from fastapi import status, HTTPException, Response, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, User, UserRole, UserUpdate
from app.repository import UsersRepository
from app.utils import oauth2
from app.dao import Users_DB_Dao
from app.utils import utils
from app.models import UserModel

users_repo = UsersRepository(Users_DB_Dao(UserModel))

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[User])
def users(db_session: Session = Depends(get_db), user=Depends(oauth2.get_current_user)):
    """
    GET ALL
    """
    if user.role != UserRole.ADMIN.value:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    local_users = users_repo.get_all(db_session)
    return local_users


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=User)
def get_user(user_id: int, db_session: Session = Depends(get_db), logged_user=Depends(oauth2.get_current_user)):
    """
    GET ID
    """
    local_user = users_repo.get_by_id(user_id, db_session)

    if not local_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    if logged_user.role == UserRole.USER and local_user.id != logged_user.id:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail=f"User id {logged_user.id} can not update user id {local_user.id}"
        )

    return local_user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: UserCreate, db_session: Session = Depends(get_db)):
    """
    POST USER
    """
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass

    if user.name is None:
        user.name = user.email

    new_user = users_repo.save(user, db_session)
    return new_user


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=User)
def update_user(
    user_id: int, user: UserUpdate, db_session: Session = Depends(get_db),
    logged_user=Depends(oauth2.get_current_user)
):
    """
    UPDATE USER
    - Verifica se o id existe // lança 404
    - Verifica se o usuário autenticado possui role = 'user' e é o mesmo da requisição // lança 405
    - Define o role = 'user' caso o usuário logado também seja user
    - Atualiza o usuário correspondente
    """

    local_user = users_repo.get_by_id(user_id, db_session)

    if not local_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    if logged_user.role == UserRole.USER.value and local_user.id != logged_user.id:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail=f"User id {logged_user.id} can not update user id {local_user.id}"
        )

    if logged_user.role == UserRole.USER.value and user.role == UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail=f"User id {logged_user.id} can not update to admin"
        )

    try:
        updated_user = users_repo.update(local_user, user, db_session)
        return updated_user

    except Exception as err:
        raise HTTPException(
            status_code=400, detail=f"{err}"
        ) from err


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db_session: Session = Depends(get_db), logged_user=Depends(oauth2.get_current_user)):
    """
    DELETE USER
    - Verifica se o id existe e lança 404 caso contrário
    - Remove o usuário com id correspondente
    """
    local_user = users_repo.get_by_id(user_id, db_session)
    if not local_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    if logged_user.role == UserRole.USER.value and local_user.id != logged_user.id:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail=f"User id {logged_user.id} can not delete user id {local_user.id}"
        )

    users_repo.delete(local_user, db_session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
