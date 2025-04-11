from fastapi import FastAPI
from app.routes import router
from app.database import engine
from app.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
