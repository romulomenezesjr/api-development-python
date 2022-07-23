from fastapi import FastAPI
from app.database import Base, engine
from app.routes import contents_router,playlists_router, users_router

# Criar as tabelas
Base.metadata.create_all(bind=engine)


# Inicia a API
app = FastAPI(
    title = "Plym Content API", 
    version = "0.0.4",
    description = "API for CRUD Content in Plym App",
    contact = { 
        "name" : "Romulo Menezes",
        "email" : "romulojnr@gmail.com",
        "url" : "http://localhost"
        } 
    )
app.include_router(contents_router.router)
app.include_router(playlists_router.router)
app.include_router(users_router.router)

