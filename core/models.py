from pydantic import BaseModel, ConfigDict
from fastapi import FastAPI

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class STaskAdd(BaseModel):
    """
    Interface on default task
    """
    name: str
    description: str | None = None

class Model(DeclarativeBase):
   pass


class STask(STaskAdd):
   id: int
   model_config = ConfigDict(from_attributes=True)

class TaskOrm(Model):
   __tablename__ = "tasks"
   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str]
   description: Mapped[str | None]

class STaskId(BaseModel):
   id: int