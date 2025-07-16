from app.models.task_model import Task
from app.db import SessionLocal
from sqlalchemy.future import select


class TaskRepository:
    async def get_all(self):
        async with SessionLocal() as session:
            result = await session.execute(select(Task))
            return result.scalars().all()

    async def create(self, title: str):
        async with SessionLocal() as session:
            task = Task(title=title)
            session.add(task)
            await session.commit()
            await session.refresh(task)
            return task.__dict__

    async def update(self, task_id: int, data: dict):
        async with SessionLocal() as session:
            task = await session.get(Task, task_id)
            if not task:
                return None
            for key, value in data.items():
                setattr(task, key, value)
            await session.commit()
            await session.refresh(task)
            return task.__dict__

    async def delete(self, task_id: int):
        async with SessionLocal() as session:
            task = await session.get(Task, task_id)
            if task:
                await session.delete(task)
                await session.commit()
