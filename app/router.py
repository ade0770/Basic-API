from fastapi import APIRouter
from fastapi.params import Depends

from app.repository import TaskRepository
from core.models import STask, STaskAdd, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)

@router.post("")
async def add_task(task: STaskAdd = Depends()) -> STaskId:
    new_task_id = await TaskRepository.add_task(task)
    return {"id": new_task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks