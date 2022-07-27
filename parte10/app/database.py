"""
This module is responsible to setup a connection using
settings and defining a session to be used - get_db
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import settings

SQLALCHEMY_DATABASE_URL = settings.database_sqlite

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = (
#     f"mysql+pymysql://"
#     f"{settings.database_username}:{settings.database_password}@"
#     f"{settings.database_hostname}:{settings.database_port}/"
#     f"{settings.database_name}"
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, )

Base = declarative_base()

# Criar as tabelas
Base.metadata.create_all(bind=engine)


def get_db():
    """Return a session and close it after."""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
