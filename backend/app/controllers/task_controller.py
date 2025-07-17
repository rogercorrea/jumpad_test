from sanic import Blueprint, response, Request
from services.task_service import TaskService

task_bp = Blueprint("tasks", url_prefix="/tasks")

@task_bp.route("/test", methods=["GET"])
async def get_test(request: Request):
    return response.text("test OK")

@task_bp.route("/", methods=["GET"])
async def get_tasks(request: Request):
    service = TaskService()
    tasks = await service.list_all()
    return response.json([dict(t) for t in tasks])

@task_bp.route("/", methods=["POST"])
async def create_task(request: Request):
    data = request.json
    service = TaskService()
    new_task = await service.create(title=data.get("title", ""))
    return response.json(new_task, status=201)

@task_bp.route("/<task_id:int>", methods=["PUT"])
async def update_task(request: Request, task_id: int):
    data = request.json
    service = TaskService()
    updated_task = await service.update(task_id, data)
    return response.json(updated_task)

@task_bp.route("/<task_id:int>", methods=["DELETE"])
async def delete_task(request: Request, task_id: int):
    service = TaskService()
    await service.delete(task_id)
    return response.empty()