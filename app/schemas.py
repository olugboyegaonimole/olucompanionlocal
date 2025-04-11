from pydantic import BaseModel
from typing import List, Optional

class EntryBase(BaseModel):
    content: str
    explanation: str

class EntryCreate(EntryBase):
    category_id: int

class EntryResponse(EntryBase):
    id: int
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    entries: List[EntryResponse] = []
    class Config:
        orm_mode = True
