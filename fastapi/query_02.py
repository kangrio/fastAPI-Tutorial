from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# การประกาศ Optional Query Parameters

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    ret = {"item_id": item_id}
    if q:
        ret.update({"q":q})
    return ret