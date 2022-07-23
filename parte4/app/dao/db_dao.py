from app.schemas import Content
from app.models import ContentModel
from app.database import get_db
class Contents_DB_Dao():
    def __init__(self):
        pass

    def getAll(self, skip:int = 0, limit:int = 10, db = next(get_db())):
        with db:
            query = db.query(ContentModel).offset(skip).limit(limit)        
            contents = query.all()
            return contents

    def getById(self, id, db = next(get_db())):
        with db:
            content = db.query(ContentModel).filter(ContentModel.id == id).first()
            return content
    
    def save(self, content, db = next(get_db())):
        with db:
            db = next(get_db())
            db_content = ContentModel(title=content.title, url=content.url)
            db.add(db_content)
            db.commit()
            db.refresh(db_content)
            return db_content
    
    def update(self, content_model, content_data, db = next(get_db())):        
        with db:
            db = next(get_db())
            content_model.title = content_data.title
            content_model.url = content_data.url
            db.commit()
            db.close()
            return content_model
    
    def delete(self, local_content, db = next(get_db())):
        with db:
            db = next(get_db())
            db.delete(local_content)
            db.commit()        