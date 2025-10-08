# from fastapi import FastAPI #imports FastAPI class

# app = FastAPI(title="Expense Tracker API") #FastAPI application instance

# @app.get("/square") # decorator: register GET "/" route on "app"

# async def calculate_square(num:int): #async handler (coroutine) named read_root 
#     return {"number": "num", "square": num**2} #return dict --> json response (200 OK)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Define a Pydantic Model for input validation

class Item (BaseModel):
    name:str
    price:float
    description: str

@app.post("/items/")

async def create_item(item:Item):
    return{"message":"Item created successfully!", "item":item}

@app.get("/")

async def read_root():
    return {"message":"Hello, World!"}