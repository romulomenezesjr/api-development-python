from typing import List
from sqlalchemy.orm import Session
from fastapi import status, HTTPException,Response, APIRouter, Depends
from app.dao import Contents_DB_Dao
from app.schemas import ContentCreate, Content
from app.repository import ContentsRepository


contents_repo = ContentsRepository(Contents_DB_Dao())

router = APIRouter(
    prefix="/contents",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", status_code = status.HTTP_200_OK, response_model = List[Content])
def contents():
    """
    GET ALL
    """
    return contents_repo.get()

@router.get("/{id}", status_code = status.HTTP_200_OK, response_model = Content)
def get_content(id: int):
    """
    GET ID
    """
    content = contents_repo.get(id)
    if not content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    return content

@router.post("/", status_code = status.HTTP_201_CREATED, response_model = Content)
def create_content(content: ContentCreate):
    """
    POST CONTENT
    """
    new_content = contents_repo.save(content)
    
    return new_content

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Content)
def update_content(id:int, content: ContentCreate):
    """
    UPDATE CONTENT
    - Verifica se o id existe e lança 404 se não existe
    - Atualiza o conteúdo correspondente
    """
    local_content = contents_repo.get(id)
    if not local_content:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Content with id {id} not found" )
    updated_content = contents_repo.update(local_content,content)
    return updated_content

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
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

