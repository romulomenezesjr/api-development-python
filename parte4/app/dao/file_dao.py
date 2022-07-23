from app.schemas import Content
from random import randint
import csv

class Contents_File_Dao():
    def __init__(self, filename = "contents.csv"):
        try:
            with open(filename, "r") as file:
                self.filename = filename
        except Exception as ex:
            print(ex)

    def getAll(self, skip = 0, limit = 10):
        local_contents = []
        with open(self.filename, "r") as file:
            content = csv.reader(file)
            for row in content:
                local_contents.append(Content(row[0], row[1]), row[2])
        return local_contents

    def getById(self, id):
        content_found = None
        with open(self.filename, "r") as file:
            content = csv.reader(file)
            for row in content:
                if int(row[0]) == id:
                    content_found = Content(row[0], row[1], row[2])

        return content_found
    
    def save(self, content):
        new_content = Content(**content.dict(), id = randint(0,100))
        with open(self.filename, "a") as file:
            content = csv.writer(file)
            for row in content:
                if int(row[0]) == id:
                    Content(row[0], row[1], row[2])
        
        return new_content
    
    def update(self, local_content, content_data):
        pass
    
    def delete(self, local_content):
        pass