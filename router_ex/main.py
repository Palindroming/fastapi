from fastapi import FastAPI
from pydantic import BaseModel as basemodel
from typing import Optional

app = FastAPI()

class Item(basemodel):
    id:int
    name:str
    price:int

class ItemUpdate(basemodel):
    id: Optional[int] = None
    name:Optional[str] = None
    price: Optional[int] = None


item_db = [
    Item(id = 1, name = "default1", price = 10000),
    Item(id = 2, name = "default2", price = 10300),
    ]


app.get("items/")
def get_items():
    return item_db

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in item_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: Item):
    item_db.append(item)
    return {"message": "Item created successfully", "item": item}







@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    for idx, existing_item in enumerate(item_db):
        if existing_item.id == item_id:
            if item.id is not None:
                existing_item.id = item.id
            if item.name is not None:
                existing_item.name = item.name
            if item.price is not None:
                existing_item.price = item.price
            return {"message": "Item updated successfully", "item": existing_item}
    return {"message": "Item not found"}








