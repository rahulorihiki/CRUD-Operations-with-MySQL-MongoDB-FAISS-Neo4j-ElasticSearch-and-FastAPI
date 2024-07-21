from fastapi import FastAPI, HTTPException
from mongo_utils import create_item, read_item, update_item, delete_item
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    on_offer: bool = False

@app.post("/items/")
def create(item: Item):
    item_id = create_item(item.dict())
    return {"item_id": item_id}

@app.get("/items/{item_id}")
def read(item_id: str):
    item = read_item(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update(item_id: str, item: Item):
    updated_item = update_item(item_id, item.dict())
    if updated_item:
        return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete(item_id: str):
    if delete_item(item_id):
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
