from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ItemStatus(Enum):
    ON_SALE = "on_sale"
    SOLD_OUT = "sold_out"

class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100, examples=["PC"])
    price: int = Field(gt=0, le=10000, examples=[1000])
    description: Optional[str] = Field(default=None,examples=["This is a PC"])

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(min_length=2, max_length=100, examples=["PC"])
    price: Optional[int] = Field(gt=0, le=10000, examples=[1000])
    description: Optional[str] = Field(default=None,examples=["This is a PC"])
    status: Optional[ItemStatus] = Field(None, examples=ItemStatus.ON_SALE)

class ItemResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    name: Optional[str] = Field(min_length=2, max_length=100, examples=["PC"])
    price: Optional[int] = Field(gt=0, le=10000, examples=[1000])
    description: Optional[str] = Field(None,examples=["This is a PC"])
    status: Optional[ItemStatus] = Field(None, examples=ItemStatus.ON_SALE)