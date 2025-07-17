from sanic import Sanic
from controllers.task_controller import task_bp
from models.task_model import Base
from db import engine

app = Sanic("TaskApp")
app.blueprint(task_bp)

@app.before_server_start
async def setup_db(app, loop):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
