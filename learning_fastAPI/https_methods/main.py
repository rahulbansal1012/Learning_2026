from fastapi import FastAPI 
import json
from dtos import product_dto

app = FastAPI(title="Https-Request")

with open("dummy_data.json" , "r") as file :
    all_product_data = json.load(file)
    
@app.post("/create_product")
def create_post(product_data : product_dto):
    product_data = product_data.model_dump()
    print(product_data)
    return {
        "status" : "product created Successfully"
    }

# put query
@app.put("/update_product_data")
def update_post(product_data : product_dto , product_id  :int):
    print("our Json Data: ",(all_product_data))
    all_products = all_product_data.get("products")

    for index,curr_product in enumerate(all_products):
        if(curr_product.get("id") == product_id):
            print("Before update" , curr_product)
            all_products[index] = product_data.model_dump()
            print("After update " , all_products[index])
            return all_products[index]
    return None
            
@app.delete("/del_product")
def delete_product(product_id : int):
    all_products = all_product_data.get("products")
    
    for index , curr_val in enumerate(all_products):
        if curr_val.get("id") == product_id : 
            deleted_record = all_products.pop(index)
            print(all_products)
            return {"delete_product" : deleted_record}



# Notes 
"""
1. we can send data in 3 ways 
    -Header
    -body
    -params

2.We need pydatic schema to validate and get the proper data from the client
Here as in creat_post(product_data:product_dto) we are using pydantic class so the input which it recieves will be the class object we need to model_dumps() to convert it into dict



"""