from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    """
    Este é o métodos home
    """
    return {"message": "hello world"}