from pydantic import BaseModel

class ContentCreate(BaseModel):
    title: str
    url: str
    class Config:
        schema_extra = {
            "example": {
                "title": "Video XZY",
                "url": "https://www.youtube.com/watch?v=4AVdTQ196cQ",        
            }
        }

class Content(ContentCreate):
    id: int
