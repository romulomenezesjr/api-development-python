from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.utils import utils, oauth2
from app.database import get_db
from app.schemas import AccessToken
from app.repository import UsersRepository
from app.dao import Users_DB_Dao
from app.models import UserModel

router = APIRouter(
    tags=["auth"]
)

user_repo = UsersRepository(Users_DB_Dao(UserModel))


@router.post("/login", response_model=AccessToken)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db)):
    """Login endpoint to authenticate users by it credentials [username, password]"""
    user_local = user_repo.get_by_email(user_credentials.username, db_session)

    if not user_local:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"user with email {user_credentials.username} not found"
        )

    if not utils.verify(user_credentials.password, user_local.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="invalid password"
        )

    access_token = oauth2.create_access_token(data={"user_id": user_local.id})
    return {"access_token": access_token, "token_type": "bearer"}
