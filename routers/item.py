from fastapi import APIRouter, Path, Query, HTTPException
from cruds import item as item_cruds
from schemas.item import ItemCreate, ItemUpdate, ItemResponse
from typing import Optional
from starlette import status

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/", response_model=list[ItemResponse],status_code=status.HTTP_200_OK)
async def find_items():
    return item_cruds.find_items()

@router.get("/{id}", response_model=Optinal[ItemResponse],status_code=status.HTTP_200_OK)
async def find_by_id(id: int=Path(gt=0)):
    found_item = item_cruds.get_item_by_id(id)
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return found_item

@router.get("/", response_model=list[ItemResponse],status_code=status.HTTP_200_OK)
async def find_by_name(name: str = Query(min_length=2, max_length=100)):
    return item_cruds.find_by_name(name)

@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item_create: ItemCreate):
    return item_cruds.create_item(item_create)

@router.put("/{id}", response_model=Optinal[ItemResponse],status_code=status.HTTP_200_OK)
async def update_item(item_update: ItemUpdate,id: int=Path(gt=0)):
    updated_item = item_cruds.get_item_by_id(id)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{id}", response_model=Optinal[ItemResponse],status_code=status.HTTP_200_OK)
async def delete_item(id: int=Path(gt=0)):
    deleted_item = item_cruds.get_item_by_id(id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted_item