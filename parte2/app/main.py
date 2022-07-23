from fastapi import FastAPI, status, HTTPException, Response
from fastapi.responses import RedirectResponse
from typing import List
from pydantic import BaseModel
from random import randint

app = FastAPI()

class ContentCreate(BaseModel):
    title: str
    url: str

class Content(ContentCreate):
    id: int

local_contents = [
    Content(id=1, title="Meu Video 1", url="https://www.youtube.com/watch?v=0sOvCWFmrtA&t=10183s&ab_channel=freeCodeCamp.org"),
    Content(id=2, title="Meu Video 2", url="https://www.youtube.com/watch?v=0sOvCWFmrtA&t=10183s&ab_channel=freeCodeCamp.org"),
    Content(id=3, title="Meu Video 3", url="https://www.youtube.com/watch?v=0sOvCWFmrtA&t=10183s&ab_channel=freeCodeCamp.org"),
]
@app.get("/")
async def home():
    """
    O método home redireciona para /docs gerado pelo fastapi/openapi
    """
    response = RedirectResponse(url='/docs')
    return response

@app.get("/contents", response_model = List[Content], status_code = status.HTTP_200_OK, response_description="List of Content",)
def contents():
    """
    GET ALL
    """
    return local_contents

@app.get("/contents/{id}", status_code = status.HTTP_200_OK, response_model = Content)
def get_content(id: int):
    """
    GET ID
    """
    # Algo 1
    #content = None
    #for c in local_contents:
    #    if c.id == id:
    #        content = c

    # Algo 2
    #content = list(filter(lambda c: c.id==id, local_contents))[0]

    content = next((c for c in local_contents if c.id == id), None)

    if not content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    return content

@app.post("/contents/", status_code = status.HTTP_201_CREATED, response_model = Content)
def create_content(content: ContentCreate):
    """
    POST CONTENT
    """
    new_content = Content(**content.dict(), id = randint(0,100))
    local_contents.append(new_content)
    
    return new_content

@app.put("/content/{id}", status_code=status.HTTP_200_OK, response_model = Content)
def update_content(id:int, content: ContentCreate):
    """
    UPDATE CONTENT
    - Verifica se o id existe e lança 404 se não existe
    - Atualiza o conteúdo correspondente
    """ 
    # Algo 1
    # index = None
    # for i,c in enumerate(local_contents):
    #     if c.id == id:
    #         index = i
    #         local_content = c
    #         break

    index, local_content = next(( (i,c) for i,c in enumerate(local_contents) if c.id==id),None) or (None,None)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )

    local_content.url = content.url
    local_content.title = content.title

    local_contents[index] = local_content

    return local_content


@app.delete("/content/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_content(id:int):
    """
    DELETE CONTENT
    - Verifica se o id existe e lança 404 se não existe
    - Remove o conteúdo com id correspondente
    """
    # Mesmo loop do update
    index, local_content = next(( (i,c) for i,c in enumerate(local_contents) if c.id==id),None) or (None,None)
    
    if local_content is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )

    local_contents.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

