from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model.stockinfo import get_stock_info

app = FastAPI()

# FastAPI uses Pydantic models to validate data.
class MessageIn(BaseModel):
    """FastAPI checks the type of the input."""
    item_id: str

@app.get("/stock-info/items/{productID}")
def stock_lookup(productID: str):
    stock = get_stock_info(productID)
    if stock:
        return stock
    return JSONResponse(status_code=404, content={"error": "Product not found"})
