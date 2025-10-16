from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model.aggregator import lookup_product

app = FastAPI()

# FastAPI uses Pydantic models to validate data.
class MessageIn(BaseModel):
    """FastAPI checks the type of the input."""
    productID: str

@app.post("/lookup")
def lookup(payload: MessageIn):
    result, status = lookup_product(payload.productID)
    return JSONResponse(status_code=status, content=result)