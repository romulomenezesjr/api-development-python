from parte7.app.database import get_db
from parte7.app.models import UserModel, ContentModel, PlaylistModel
from parte7.app.utils import utils

users = [
    {
    "id": 1,
    "email": "admin@admin.com",
    "password": utils.hash ("admin"),
    "name": "Admin",
    "role" : "admin"
    },
    {
    "id": 2,
    "email": "user@user.com",
    "password": utils.hash ("user"),
    "name": "User",
    "role" : "user"
    },
    {
    "id": 3,
    "email": "none@none.com",
    "password": utils.hash ("none"),
    "name": "none",
    "role" : "user"
    },
]

playlists = [
    {
        "id": 1,
        "title": "Admin playlist",
        "description": "Description of the admin playlist",
        "thumbnail": "",
        "published": True,
        "user_id" : 1,
    },
    {
        "id": 2,
        "title": "User playlist",
        "description": "Description of the user playlist",
        "thumbnail": "",
        "published": True,
        "user_id" : 2,
    }
]

contents = [
    {
        "id": 1,
        "title": "Content of admin playlist",
        "url": "nourl",
        "playlist_id":1
    },
    {
        "id": 2,
        "title": "First content on user playlist",
        "url": "nourl",
        "playlist_id": 2
    },
    {
        "id": 3,
        "title": "Seccond content on user playlist",
        "url": "nourl",
        "playlist_id": 2
    },
    {
        "id": 4,
        "title": "Third content on user playlist",
        "url": "nourl",
        "playlist_id": 2
    }
]

def data_load(delete_on_startup = False):   
    db = next(get_db())
    
    if len(db.query(UserModel).all()) == 0:
        try:
            for user in users:
                db.add(UserModel(**user))
            db.commit()
            db.refresh(user)    
        except Exception as err:   
            print(err)        
            db.rollback()

    if len(db.query(PlaylistModel).all()) == 0:
        try:
            for playlist in playlists:
                db.add(PlaylistModel(**playlist))
            db.commit()
            db.refresh(playlist)    
        except Exception as err:   
            print(err)        
            db.rollback()

    if len(db.query(ContentModel).all()) == 0:
        try:
            for content in contents:
                db.add(ContentModel(**content))
            db.commit()
            db.refresh(content)    
        except Exception as err:   
            print(err)        
            db.rollback()


from parte7.app.database import engine
from sqlalchemy import text
def script_load():
    with engine.connect() as con:
        with open("app/utils/query.sql", "r") as file:
            for line in file:
                query = text(line)
                try:
                    con.execute(query)
                except Exception as err:
                    print(err)


