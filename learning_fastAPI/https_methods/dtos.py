from pydantic import BaseModel

class product_dto(BaseModel):
    id : int 
    title :str
    price :float = 0
    count : int  = 0