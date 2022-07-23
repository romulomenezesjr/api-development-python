from abc import ABC, abstractmethod
from typing import Any, List

class Repository(ABC):

    def __init__(self, dao):
        self.dao = dao

    def getAll(self, skip = 0, limit = 10):
        return self.dao.getAll(skip, limit)
    
    def getById(self, id: int):
        return self.dao.getById(id)

    def get(self, id=None, skip = 0, limit = 10):
        if id:
            self.getById(id)
        else:
            self.getAll(skip, limit)

    def save(self, schema):
        return self.dao.save(schema)

    def update(self, model_ddata, schema_data):
        return self.dao.update(model_ddata, schema_data)

    def delete(self, model_data):
        self.dao.delete(model_data)
    
class ContentsRepository(Repository):
    
    def getByTitle(self, title):
        return self.dao.getByTitle(title)


    