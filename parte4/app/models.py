from app.database import Base
from sqlalchemy import Column, Integer, String 

class ContentModel(Base):
    __tablename__ = "contents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True )
    url = Column(String(255), index=True)
    