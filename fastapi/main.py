from fastapi import FastAPI
from enum import Enum, IntEnum
from fastapi.responses import *

app = FastAPI()

# root
@app.get("/")
def root():
    return {'Hello' : 'My love'}

# Items ID
@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id": item_id}

# Order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



################################################################
@app.get("/reload")
def reload():
    return ['Reloading !!!']

@app.get("/myname/{name}")
def myname(name : str):
    return {'Hello' : name}


###########################################################################

# Getfile
@app.get("/getfile")
def getfile():
    filename = 'video.mp4'
    return FileResponse(filename)

#StreamingVideo
@app.get("/streamvideo")
def streamvideo():
    filename = 'video.mp4'
    def iterfile():  
        with open(filename, mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="video/mp4")
