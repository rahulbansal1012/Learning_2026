from fastapi import APIRouter ,Depends
from src.task import controller 
from src.task.dtos import TaskSchema
from src.utils.db import get_db
task_router = APIRouter(prefix= "/tasks")

@task_router.post("/create")
def create_task(input_data : TaskSchema , db = Depends(get_db)):
    return controller.create_task(input_data , db)