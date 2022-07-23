from typing import List, Union
from fastapi import status, HTTPException,Response
from app.repository import ContentsRepository
from app.schemas import ContentCreate, Content
from app.dao import Memory_Dao
from app.main import app

contents_repo = ContentsRepository(Memory_Dao())

@app.get("/contents",  status_code = status.HTTP_200_OK, response_model = List[Content])
def contents(skip: int = 0, limit: Union[int, None] = None):
    """
    GET ALL
    """
    return contents_repo.getAll(skip=skip, limit=limit)

@app.get("/contents/{id}", status_code = status.HTTP_200_OK, response_model = Content)
def get_content(id: int):
    """
    GET ID
    """
    content = contents_repo.get(id)
    if not content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    return content

@app.post("/contents/", status_code = status.HTTP_201_CREATED, response_model = Content)
def create_content(content: ContentCreate):
    """
    POST CONTENT
    """
    new_content = contents_repo.save(content)
    
    return new_content

@app.put("/content/{id}", status_code=status.HTTP_200_OK, response_model=Content)
def update_content(id:int, new_content: ContentCreate):
    """
    UPDATE CONTENT
    - Verifica se o id existe e lança 404 se não existe
    - Atualiza o conteúdo correspondente
    """
    local_content = contents_repo.get(id)
    if not local_content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    
    updated_content = contents_repo.update(local_content, new_content)
    return updated_content

@app.delete("/content/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_content(id:int):
    """
    DELETE CONTENT
    - Verifica se o id existe e lança 404 se não existe
    - Remove o conteúdo com id correspondente
    """
    local_content = contents_repo.get(id)
    if not local_content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    contents_repo.delete(local_content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

