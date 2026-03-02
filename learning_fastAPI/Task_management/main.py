from fastapi import FastAPI
from src.utils.db import engine,Base
import psycopg
from src.task.model import TaskModel
from src.task.router import task_router
Base.metadata.create_all(engine)

app = FastAPI(title= "Task Management App")
app.include_router(task_router)