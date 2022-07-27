import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.schemas import Playlist, User
from app.database import get_db, Base
from app.main import app
from app.models import PlaylistModel, UserModel
from app.utils import utils

"""
Arquivo conftest.py é importado automaticamente por outros testes no mesmo pacote
"""
from app.utils.oauth2 import create_access_token

@pytest.fixture
def token(client, test_user):
    return create_access_token({"user_id": test_user.id})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client 

@pytest.fixture
def test_user(session):
    # Change to replace using client to use a direct insertion to the database
    
    # res = client.post("/users/", json={"email":"romulo@gmail.com", "password":"remo"})
    # assert res.status_code == status.HTTP_201_CREATED
    # return User(**res.json())
    user_db = UserModel(**{"email":"romulo@gmail.com", "password": utils.hash("remo")})
    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return User(email = user_db.email, password=user_db.password, id = user_db.id)

@pytest.fixture
def test_playlists(test_user,session):
    # Change to replace using client to use a direct insertion to the database
    
    # res = authorized_client.post("/playlists/", json={
    #     "title": "Test ",
    #     "thumbnail": "",
    #     "description": "test playlist",
    #     "published": "True"
    # })

    playlist_db = PlaylistModel(title="Test", thumbnail="", description="", published=True, user_id = test_user.id)
    session.add(playlist_db)
    session.commit()
    session.refresh(playlist_db)
    return playlist_db

@pytest.fixture
def session():
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app_test.db?check_same_thread=False"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, )
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def get_db_test():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = get_db_test
    yield TestClient(app)

