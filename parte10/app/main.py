"""
Main module to start the api.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.settings import settings
from app.routes import contents_router, playlists_router
from app.routes import users_router, auth_router, likes_router

# app.utilsdata_inicialization.data_load()

# Inicia a API
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description,
    contact={
        "name": settings.api_contact_name,
        "email": settings.api_contact_email,
        "url": settings.api_contact_url
    }
)

# Configura CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    """Home endpoint of the api"""
    return {"message": "hello world"}


app.include_router(contents_router.router)
app.include_router(playlists_router.router)
app.include_router(users_router.router)
app.include_router(auth_router.router)
app.include_router(likes_router.router)
