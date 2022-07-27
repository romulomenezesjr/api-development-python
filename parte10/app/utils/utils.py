from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    """Hash password with bcrypt."""
    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str):
    """Verify if plain password is equals to hashed password with bcrypt."""
    return pwd_context.verify(plain_password, hashed_password)
