import pytest
from sanic import Sanic
from sanic.testing import SanicTestClient
from app.main import app

@pytest.fixture
def test_cli():
    return SanicTestClient(app)

@pytest.mark.asyncio
async def test_get_tasks(test_cli):
    request, response = await test_cli.get("/tasks/")
    assert response.status == 200
    assert isinstance(response.json, list)

@pytest.mark.asyncio
async def test_create_update_delete_task(test_cli):
    req, res = await test_cli.post("/tasks/", json={"title": "Test Task"})
    assert res.status == 201
    task = res.json
    assert task["title"] == "Test Task"
    task_id = task["id"]

    req, res = await test_cli.put(f"/tasks/{task_id}", json={"completed": True})
    assert res.status == 200
    assert res.json["completed"] == True

    req, res = await test_cli.delete(f"/tasks/{task_id}")
    assert res.status == 204
