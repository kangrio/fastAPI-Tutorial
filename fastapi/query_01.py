from fastapi import FastAPI

app = FastAPI()

items = [
    {"item_name": "item1"},
    {"item_name": "item2"},
    {"item_name": "item3"},
]

# การประกาศ Query Parameters

@app.get("/items/{search}")
async def read_item(search: str, skip: int = 0, limit: int = 10):
    return {"search": search, "result": items[ skip : skip + limit]}

