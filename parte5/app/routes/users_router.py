from typing import List
from fastapi import status, HTTPException,Response, APIRouter, Depends
from app.repository import UsersRepository
from app.utils import utils
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import User, UserCreate
from app.dao import Users_DB_Dao
from app.models import UserModel

userRepo = UsersRepository(Users_DB_Dao(UserModel))

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", status_code = status.HTTP_200_OK, response_model = List[User])
def users(db = Depends(get_db)):
    """
    GET ALL
    """
    return userRepo.getAll(db)

@router.get("/{id}", status_code = status.HTTP_200_OK, response_model = User)
def get_user(id: int, db = Depends(get_db)):
    """
    GET ID
    """
    user = userRepo.getById(id, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found" )
    return user

@router.post("/", status_code = status.HTTP_201_CREATED, response_model = User)
def create_user(user: UserCreate, db = Depends(get_db)):
    """
    POST USER
    """
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass
    try:
        new_user = userRepo.save(user, db)
        return new_user
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err.orig}")

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=User)
def update_user(id:int, user: UserCreate, db = Depends(get_db)):
    """
    UPDATE USER
    - Verifica se o id existe e lança 404 caso contrário
    - Atualiza o usuário correspondente
    """
    local_user = userRepo.getById(id, db)
    if not local_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found" )
    try:
        updated_user = userRepo.update(local_user, user, db)
        return updated_user
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err.orig}")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int, db = Depends(get_db)):
    """
    DELETE USER
    - Verifica se o id existe e lança 404 caso contrário
    - Remove o usuário com id correspondente
    """
    local_user = userRepo.getById(id, db)
    if not local_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found" )
    try:
        userRepo.delete(local_user, db)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err.orig}")

