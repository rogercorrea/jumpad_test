from sanic import Sanic
from sanic_cors import CORS
from controllers.task_controller import task_bp
from models.task_model import Base
from db import engine

app = Sanic("TaskApp")
CORS(app)  # Habilita CORS para todas as rotas

app.blueprint(task_bp)

@app.before_server_start
async def setup_db(app, loop):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
