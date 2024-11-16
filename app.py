import datetime
from pydantic import BaseModel


class Order(BaseModel):
    number : int
    startDate : datetime.date
    device : str
    problemType : str
    description: str
    client : str
    status : str

repo = [
    Order(
        number = 1,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    )
]

from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/orders")
def get_orders():
    return repo