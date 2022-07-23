from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router 

# Cria as tabelas
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
# Inclui a rota
app.include_router(router)

