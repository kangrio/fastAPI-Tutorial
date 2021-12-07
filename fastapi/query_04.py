from fastapi import FastAPI
from typing import Optional


app = FastAPI()


#  Multiple path and query parameters

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    item_id: str,
    user_id: int,
    q: Optional[str] = None,
    short: bool = False,
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({
            "description": "ได้หมด"
        })
    return item


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     item_id: str,
#     user_id: int,
#     q: Optional[str] = None,
#     short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "คําอธิบายจ้า"}
#         )
#     return item
