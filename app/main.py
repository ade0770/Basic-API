from fastapi import FastAPI, Depends
from core.models import STaskAdd

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_tables, delete_tables

from app.router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

@app.get("/")
async def home():
    return {"data": "Hello World"}

@app.post("/")
async def add_task(task: STaskAdd = Depends()):
    return {"data": task}