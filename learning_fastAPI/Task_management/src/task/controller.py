from src.task.dtos import TaskSchema
from src.utils.db import get_db
from sqlalchemy.orm import session
from src.task.model import TaskModel 
def create_task(body : TaskSchema, db :session ):
    data =  body.model_dump()
    new_task = TaskModel(title = data["title"] ,description = data["description"], is_completed = data["is_completed"])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {
        "status" :f"Task created 100%  {new_task}"
    }