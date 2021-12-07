from fastapi import FastAPI
from random import randint

app = FastAPI()


#  Boolean Types Conversion

@app.get("/magic")
async def read_item(lotto:bool=False):
    item = {"lotto":lotto}
    if lotto:
        mnum:str = str(randint(1,999)).zfill(3)
        item.update({
            "number" : f"งวดนี้แม่นๆจ้า {mnum}"
        })
    return item