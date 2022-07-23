from app.schemas import Content
from random import randint

class Memory_Dao:
    def __init__(self):
        self.local_contents = [
            Content(id=1, title="Meu Video 1", url="https://www.youtube.com/watch?v=0sOvCWFmrtA&t=10183s&ab_channel=freeCodeCamp.org"),
            Content(id=2, title="Meu Video 2", url="https://www.youtube.com/watch?v=0sOvCWFmrtA&t=10183s&ab_channel=freeCodeCamp.org"),
            Content(id=3, title="Meu Video 3", url="https://www.youtube.com/watch?v=0sOvCWFmrtA&t=10183s&ab_channel=freeCodeCamp.org"),
        ]

    def getAll(self, skip = 0, limit = 10):
        return self.local_contents[skip:][:limit]

    def getById(self, id):
        # Algo 1
        #content = None
        #for c in self.local_contents:
        #    if c.id == id:
        #        content = c

        # Algo 2
        #content = list(filter(lambda c: c.id==id, self.local_contents))[0]

        content = next((c for c in self.local_contents if c.id == id), None)
        return content
    
    def save(self, content):
        new_content = Content(**content.dict(), id = randint(0,100))
        self.local_contents.append(new_content)
        return new_content
    
    def update(self, local_content, content_data):
        local_content.url = content_data.url
        local_content.title = content_data.title
        return local_content
    
    def delete(self, local_content):
        # Algo 1
        # index = None
        # for i, c in enumerate(self.local_contents):
        #     if c.id == local_content.id:
        #        index = i        
        index,_ = next(( (i,c) for i,c in enumerate(self.local_contents) if c.id==local_content.id),None) or (None,None)
        self.local_contents.pop(index)