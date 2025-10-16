from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model.iteminfo import get_item_info

app = FastAPI()

# FastAPI uses Pydantic models to validate data.
class MessageIn(BaseModel):
    """FastAPI checks the type of the input."""
    item_id: str

@app.get("/item-info/items/{productID}")
def item_lookup(productID: str):
    item = get_item_info(productID)
    if item:
        return item
    return JSONResponse(status_code=404, content={"error": "Product not found"})