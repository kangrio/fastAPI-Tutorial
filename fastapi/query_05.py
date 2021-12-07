from fastapi import FastAPI
from typing import Optional


app = FastAPI()


#  Required query parameters

@app.get("/items/{item_id}")
async def read_user_item(
    item_id:str,
    needy:str,
):
    item = {"item_id":item_id,"needy": needy}
    return item
    