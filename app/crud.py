from sqlalchemy.orm import Session
from . import models, schemas

def get_categories(db: Session):
    return db.query(models.Category).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_entries(db: Session, category_id: int):
    return db.query(models.Entry).filter(models.Entry.category_id == category_id).all()

def create_entry(db: Session, entry: schemas.EntryCreate):
    db_entry = models.Entry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
