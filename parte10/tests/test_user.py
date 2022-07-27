from jose import jwt
import pytest
from app import schemas
from app import settings
from fastapi import status

"""
Testes:
- Criar um usuário
- Login de um usuário existente
- Falha de login de um usuário existente
...
"""

@pytest.mark.parametrize("email, password", [
    ("romulo@gmail.com", "remo"),
    ("remo@gmail.com", "romulo")
])
def test_create_user(client, email, password):
    res = client.post("/users/", json={"email": email, "password": password})
    user_schema = schemas.User(**res.json())
    assert user_schema.role == schemas.UserRole.USER.value
    assert res.status_code == status.HTTP_201_CREATED

def test_login(test_user, client):
    res = client.post("/login", data={"username":test_user.email, "password":"remo"})
    token = schemas.AccessToken(**res.json())
    login_user = jwt.decode(token.access_token, settings.settings.jwt_secret_key, algorithms=[settings.settings.jwt_algorithm])
    assert login_user["user_id"] == test_user.id
    assert res.status_code == status.HTTP_200_OK
    
@pytest.mark.parametrize("email, password, status_code", [
    ("romulo@gmail.com", "aaaaaaaaaaaaaaaaaaaa", status.HTTP_403_FORBIDDEN),
    ("remo@gmail.com", None, status.HTTP_422_UNPROCESSABLE_ENTITY)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username":email, "password":password})
    
    assert res.status_code == status_code
    # assert res.json().get("detail") == "invalid password"