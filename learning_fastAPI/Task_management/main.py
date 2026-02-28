from fastapi import FastAPI
from src.utils.db import engine,Base
import psycopg
from src.task.model import TaskModel

Base.metadata.create_all(engine)

app = FastAPI(title= "Task Management App")