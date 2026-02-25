from fastapi import FastAPI,HTTPException,Request
import json 
from http import HTTPStatus
with open("dummy_data.json" , "r") as file :
    product_data = json.load(file)

# print((product_data))
 
app = FastAPI(title= "My Basic API")

@app.get("/")
def home():
    return "Welcome to the home page"
# Get all products 
@app.get("/products")
def get_all_products():
    return product_data

# Params are of 2 type 
# 1.Path Params -> Identify resource  for ex Get user with id 101 {/}
# 2. Query Params -> Fileter Resource for ex get user from india {?}

# Get particular products with the help of path params 
@app.get("/products/{product_id}")
def get_particular_product(product_id:int):

    for product in product_data.get("products"):
        if(product_id == product.get("id") ):
            return product
    raise HTTPException(
            status_code = HTTPStatus.NOT_FOUND,
            detail="Product not found"
        )

# This fucntion is using the basic hardcoded params best for known params
# @app.get("/product")
# def get_products_based_on_price(price : float):
#     output_product= []
#     for product in product_data.get("products"):
#         if (product.get("price")>price):
#             output_product.append(product)
#     return output_product

# This fucntion depict that we should use Request as Request haev access to all the metadata which are passed in the Request
@app.get("/product")
def get_particular_product_request(request:Request) :
    query_params = dict(request.query_params)
    print(query_params)
    output_product= []
    for product in product_data.get("products"):
        if (product.get("price")> float(query_params.get("price"))):
            output_product.append(product)
    return output_product