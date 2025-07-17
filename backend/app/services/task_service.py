from repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    async def list_all(self):
        return await self.repo.get_all()

    async def create(self, title: str):
        return await self.repo.create(title)

    async def update(self, task_id: int, data: dict):
        return await self.repo.update(task_id, data)

    async def delete(self, task_id: int):
        return await self.repo.delete(task_id)