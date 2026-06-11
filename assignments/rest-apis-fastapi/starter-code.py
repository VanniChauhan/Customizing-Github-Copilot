from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI()

# TODO: Define a Pydantic model for your resource
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float

# TODO: Create an in-memory database (a simple list or dictionary)
# Example:
# items_db = []

# TODO: Implement the root endpoint
# @app.get("/")
# def read_root():
#     pass

# TODO: Implement a simple GET endpoint with a query parameter
# @app.get("/greet")
# def greet(name: str):
#     pass

# TODO: Implement POST endpoint to create a new resource
# @app.post("/items/")
# def create_item(item: Item):
#     pass

# TODO: Implement GET endpoint to retrieve all resources
# @app.get("/items/")
# def read_items():
#     pass

# TODO: Implement GET endpoint to retrieve a single resource by ID
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     pass

# TODO: Implement PUT endpoint to update a resource
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     pass

# TODO: Implement DELETE endpoint to remove a resource
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     pass

# Run with: uvicorn starter-code:app --reload
