from core.models import TaskOrm
from app.database import new_session
from sqlalchemy import select

from core.models import STaskAdd, STask

# async def add_task(data: dict) -> int:
#     """
#     Adds new Task
#     :param data:
#     :return: id
#     """
#     async with new_session() as session:
#         new_task = TaskOrm(**data)
#         session.add(new_task)
#
#         await session.flush() # ~ INSERT INTO tasks (name,description) VALUES ('Jack', NULL) RETURNING id
#         await session.commit() # commit changes in DB, end transaction
#
#         return new_task.id
#
# async def get_tasks():
#
#    async with new_session() as session:
#        query = select(TaskOrm)
#        result = await session.execute(query) # iterator
#        task_models = result.scalars().all() # we go through the iterator and get all required results
#        return task_models

class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskOrm(**data)
            session.add(new_task)

            await session.flush()  # ~ INSERT INTO tasks (name,description) VALUES ('Jack', NULL) RETURNING id
            await session.commit()  # commit changes in DB, end transaction

            return new_task.id

    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)  # iterator
            task_models = result.scalars().all()  # we go through the iterator and get all required results
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return task_models

