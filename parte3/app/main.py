from fastapi import FastAPI

app = FastAPI(
    title="Plym Content API", 
    version="0.0.3",
    description="API for CRUD Content in Plym App",
    contact={
        "name":"Romulo Menezes",
        "email":"romulojnr@gmail.com",
        "url":"http://localhost"
    } 
)

@app.get("/")
def home():
    return {"message": "hello world"}

from app.routes import contents_route