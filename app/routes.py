from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, database

router = APIRouter()

@router.get("/categories", response_model=list[schemas.CategoryResponse])
def read_categories(db: Session = Depends(database.get_db)):
    return crud.get_categories(db)

@router.post("/categories", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    return crud.create_category(db, category)

@router.get("/entries", response_model=list[schemas.EntryResponse])
def read_entries(category_id: int, db: Session = Depends(database.get_db)):
    return crud.get_entries(db, category_id)

@router.post("/entries", response_model=schemas.EntryResponse)
def create_entry(entry: schemas.EntryCreate, db: Session = Depends(database.get_db)):
    return crud.create_entry(db, entry)
